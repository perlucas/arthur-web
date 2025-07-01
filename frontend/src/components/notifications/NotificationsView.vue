<script setup>
  import { ref, onMounted } from 'vue';
  import Layout from '../layout/user/Layout.vue';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  import Button from 'primevue/button';
  import { useNotifications } from './useNotifications';
  import { useDateFns } from '../../composables/useDateFns';
  import { useI18n } from 'vue-i18n';

  const { t } = useI18n();
  const { notifications, totalRecords, loading, fetchNotifications, toggleRead, deleteNotification } =
    useNotifications();
  const { formatDate } = useDateFns();

  const selectedNotifications = ref([]);
  const lazyParams = ref({});

  onMounted(() => {
    lazyParams.value = {
      first: 0,
      rows: 10,
      sortField: 'timestamp',
      sortOrder: -1,
    };
    loadLazyData();
  });

  const loadLazyData = async () => {
    const page = lazyParams.value.first / lazyParams.value.rows;
    await fetchNotifications(page, lazyParams.value.rows);
  };

  const onPage = (event) => {
    lazyParams.value = event;
    loadLazyData();
  };

  const handleToggleRead = async (notification) => {
    await toggleRead(notification.id, !notification.isRead);
    // Optimistically update the UI
    notification.isRead = !notification.isRead;
  };

  const handleDelete = async (notification) => {
    await deleteNotification(notification.id);
    loadLazyData(); // Refresh data
  };

  const getRowClass = (data) => {
    return { 'font-bold': !data.isRead };
  };
</script>

<template>
  <Layout :title="t('notificationsView.title')">
    <main class="p-6">
      <!-- Header -->
      <div class="mb-6">
        <h1 class="text-2xl font-bold text-white">{{ t('notificationsView.title') }}</h1>
        <p class="text-gray-400 mt-1">{{ t('notificationsView.subtitle') }}</p>
      </div>

      <!-- Bulk Actions -->
      <div v-if="selectedNotifications.length > 0" class="mb-2 flex flex-col">
        <div class="flex gap-2 mb-1">
          <button
            class="bg-red-500 hover:bg-red-700 text-white px-4 py-2 rounded-lg flex items-center transition-colors duration-200"
          >
            <i class="pi pi-trash mr-2" />
            {{ t('notificationsView.bulkActions.deleteAll') }}
          </button>
          <button
            class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg flex items-center transition-colors duration-200"
          >
            <i class="pi pi-eye mr-2" />
            {{ t('notificationsView.bulkActions.markAllRead') }}
          </button>
          <button
            class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg flex items-center transition-colors duration-200"
          >
            <i class="pi pi-eye-slash mr-2" />
            {{ t('notificationsView.bulkActions.markAllUnread') }}
          </button>
        </div>
        <span class="text-gray-400">{{ t('notificationsView.bulkActions.selected', { count: selectedNotifications.length }) }}</span>
      </div>

      <!-- Table -->
      <div class="rounded-lg border border-gray-700 bg-gray-800 shadow-lg p-4">
        <DataTable
          v-model:selection="selectedNotifications"
          :value="notifications"
          :total-records="totalRecords"
          :loading="loading"
          lazy
          paginator
          :rows="10"
          :rows-per-page-options="[10, 20, 50]"
          @page="onPage"
          :row-class="getRowClass"
          class="p-datatable-sm"
        >
          <Column selection-mode="multiple" header-style="width: 3rem"></Column>
          <Column :header="t('notificationsView.table.timestamp')" style="width: 20%">
            <template #body="{ data }">
              {{ formatDate(data.timestamp) }}
            </template>
          </Column>
          <Column :header="t('notificationsView.table.message')">
            <template #body="{ data }">
              <div v-html="data.message"></div>
            </template>
          </Column>
          <Column :header="t('notificationsView.table.actions')" style="width: 10rem">
            <template #body="{ data }">
              <div class="flex items-center space-x-2">
                <Button
                  :icon="data.isRead ? 'pi pi-eye-slash' : 'pi pi-eye'"
                  class="p-button-rounded p-button-text"
                  @click="handleToggleRead(data)"
                  v-tooltip.top="data.isRead ? t('notificationsView.tooltips.markAsUnread') : t('notificationsView.tooltips.markAsRead')"
                />
                <Button
                  icon="pi pi-trash"
                  class="p-button-rounded p-button-text p-button-danger"
                  @click="handleDelete(data)"
                  v-tooltip.top="t('notificationsView.tooltips.delete')"
                />
              </div>
            </template>
          </Column>
        </DataTable>
      </div>
    </main>
  </Layout>
</template>

<style scoped>
  :deep(.p-paginator-rpp-dropdown) {
    background-color: var(--color-gray-900);
  }
  :deep(.font-bold) {
    font-weight: 700;
  }
</style>
