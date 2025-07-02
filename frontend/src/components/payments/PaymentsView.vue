<script setup>
  import { ref, onMounted } from 'vue';
  import Layout from '../layout/user/Layout.vue';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  import { usePayments } from './usePayments';
  import { useDateFns } from '../../composables/useDateFns';
  import { useI18n } from 'vue-i18n';

  const { t } = useI18n();
  const { payments, totalRecords, loading, fetchPayments } = usePayments();
  const { formatDate } = useDateFns();

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
    await fetchPayments(page, lazyParams.value.rows);
  };

  const onPage = (event) => {
    lazyParams.value = event;
    loadLazyData();
  };

  const formatCurrency = (value) => {
    return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value);
  };
</script>

<template>
  <Layout :title="t('paymentsView.title')">
    <main class="p-6">
      <!-- Header -->
      <div class="mb-6">
        <h1 class="text-2xl font-bold text-white">{{ t('paymentsView.title') }}</h1>
        <p class="text-gray-400 mt-1">{{ t('paymentsView.subtitle') }}</p>
      </div>

      <!-- Table -->
      <div
        v-if="payments.length > 0"
        class="rounded-lg border border-gray-700 bg-gray-800 shadow-lg p-4"
      >
        <DataTable
          :value="payments"
          :total-records="totalRecords"
          :loading="loading"
          lazy
          paginator
          :rows="10"
          :rows-per-page-options="[10, 20, 50]"
          @page="onPage"
          class="p-datatable-sm"
        >
          <Column :header="t('paymentsView.table.date')" style="width: 20%">
            <template #body="{ data }">
              {{ formatDate(data.timestamp, 'PPP') }}
            </template>
          </Column>
          <Column :header="t('paymentsView.table.description')">
            <template #body="{ data }">
              {{ data.description }}
            </template>
          </Column>
          <Column :header="t('paymentsView.table.amount')" style="width: 15%">
            <template #body="{ data }">
              <span class="font-semibold">{{ formatCurrency(data.amount) }}</span>
            </template>
          </Column>
        </DataTable>
      </div>
      <div v-else class="rounded-lg border border-gray-700 bg-gray-800 p-2">
        <p class="text-center text-gray-400">{{ t('paymentsView.empty') }}</p>
      </div>
    </main>
  </Layout>
</template>

<style scoped>
  :deep(.p-paginator-rpp-dropdown) {
    background-color: var(--color-gray-900);
  }
</style>
