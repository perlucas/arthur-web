<script setup>
  import { ref, watch } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import Layout from '../layout/user/Layout.vue';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  import PreviousResultsModal from './PreviousResultsModal.vue';
  import { useI18n } from 'vue-i18n';
  import { useDateFns } from '@/composables/useDateFns';

  const { t } = useI18n();
  const { formatDistance, formatDate } = useDateFns();

  const router = useRouter();
  const route = useRoute();
  const searchId = +route.params?.searchId || -1;

  watch(
    () => searchId,
    (searchId) => {
      if (searchId === -1) {
        router.push('/error-404');
      }
    },
    { immediate: true },
  );

  const jobSearch = ref({
    id: 1,
    name: 'Senior Frontend Developer',
    lastUpdated: new Date(Date.now() - 2 * 60 * 60 * 1000),
    isActive: true,
  });

  const results = ref([
    {
      platform: 'LinkedIn',
      url: 'https://www.linkedin.com/jobs/view/1234567890/',
      timestamp: new Date(Date.now() - 3 * 60 * 60 * 1000),
    },
    {
      platform: 'LinkedIn',
      url: 'https://www.linkedin.com/jobs/view/1234567891/',
      timestamp: new Date(Date.now() - 4 * 60 * 60 * 1000),
    },
    {
      platform: 'LinkedIn',
      url: 'https://www.linkedin.com/jobs/view/1234567892/',
      timestamp: new Date(Date.now() - 5 * 60 * 60 * 1000),
    },
    {
      platform: 'CompuTrabajo',
      url: 'https://www.computrabajo.com/jobs/view/1234567890/',
      timestamp: new Date(Date.now() - 8 * 60 * 60 * 1000),
    },
    {
      platform: 'Indeed',
      url: 'https://www.indeed.com/jobs/view/1234567890/',
      timestamp: new Date(Date.now() - 12 * 60 * 60 * 1000),
    },
  ]);

  const previousResultsModalVisible = ref(false);

  const onShowPreviousResults = () => {
    previousResultsModalVisible.value = true;
  };

  const isDemo = ref(false); // TODO: implement
</script>

<template>
  <Layout :title="t('searchResults.title')">
    <main class="p-6">
      <!-- Header -->
      <div class="flex items-center mb-6">
        <div class="flex-1">
          <h1 class="mb-2 text-2xl font-bold text-white">{{ jobSearch.name }}</h1>
          <div class="flex items-center text-sm text-gray-400">
            <div class="mr-4 flex items-center">
              <div
                :class="jobSearch.isActive ? 'bg-green-500' : 'bg-gray-500'"
                class="mr-2 h-3 w-3 rounded-full"
              ></div>
              <span :class="jobSearch.isActive ? 'text-green-400' : 'text-gray-400'">
                {{ jobSearch.isActive ? t('searchResults.active') : t('searchResults.paused') }}
              </span>
            </div>
            <div class="flex items-center">
              <i class="pi pi-calendar mr-2" />
              {{ t('searchResults.updated') }}
              {{ formatDistance(jobSearch.lastUpdated) }}
            </div>
          </div>
        </div>

        <button
          class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg flex items-center transition-colors duration-200"
          @click="onShowPreviousResults"
        >
          <i class="pi pi-history mr-2" />
          {{ t('searchResults.previousResults') }}
        </button>
      </div>

      <!-- Export as CSV  -->
      <div v-if="results.length > 0 && !isDemo" class="flex justify-start my-4">
        <button class="rounded-md bg-blue-600 hover:bg-blue-700 text-white px-4 py-2">
          <i class="pi pi-download mr-2" />
          {{ t('searchResults.exportCSV') }}
        </button>
      </div>

      <!-- Results Table -->
      <div
        v-if="results.length > 0"
        class="rounded-lg border border-gray-700 bg-gray-800 shadow-lg p-2"
      >
        <DataTable
          :value="results"
          sort-mode="multiple"
          paginator
          :rows="10"
          :rows-per-page-options="[10, 20, 50]"
          class="p-datatable-sm"
          row-hover
        >
          <Column :field="t('searchResults.platform')" header="Platform" sortable>
            <template #body="slotProps">
              <span class="font-semibold">{{ slotProps.data.platform }}</span>
            </template>
          </Column>
          <Column :field="t('searchResults.url')" header="URL">
            <template #body="slotProps">
              <a
                :href="slotProps.data.url"
                target="_blank"
                rel="noopener noreferrer"
                class="text-blue-400 hover:text-blue-300 hover:underline"
              >
                {{ slotProps.data.url }}
              </a>
            </template>
          </Column>
          <Column :field="t('searchResults.timestamp')" header="Timestamp" sortable>
            <template #body="slotProps">
              {{ formatDate(slotProps.data.timestamp) }}
            </template>
          </Column>
        </DataTable>
      </div>
      <div v-else class="rounded-lg border border-gray-700 bg-gray-800 p-2">
        <p class="text-center text-gray-400">
          {{ t('searchResults.noResultsMessage') }}
        </p>
      </div>
    </main>
    <PreviousResultsModal v-model:visible="previousResultsModalVisible" :search-id="searchId" />
  </Layout>
</template>

<style scoped>
  :deep(.p-paginator-rpp-dropdown) {
    background-color: var(--color-gray-900);
  }
</style>
