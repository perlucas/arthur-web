<script setup>
  import { Dialog } from 'primevue';
  import { ref, onMounted } from 'vue';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  import Button from 'primevue/button';
  import ProgressSpinner from 'primevue/progressspinner';
  import { useI18n } from 'vue-i18n';
  import { useDateFns } from '@/composables/useDateFns';

  const { formatDistance, formatDate } = useDateFns();
  const { t } = useI18n();
  const visible = defineModel({ default: false, type: Boolean });

  const { searchId } = defineProps({
    searchId: { type: Number, required: true },
  });

  const loading = ref(true);
  const previousResultFiles = ref([]);

  onMounted(() => {
    console.log(`Fetching previous results for search ID: ${searchId}`);

    // Simulate API call
    setTimeout(() => {
      previousResultFiles.value = [
        {
          timestamp: new Date(Date.now() - 3 * 60 * 60 * 1000),
          csvUrl:
            'https://www.stats.govt.nz/assets/Uploads/Business-operations-survey/Business-operations-survey-2023/Download-data/business-operations-survey-2023-CSV-notes.xlsx',
          resultsCount: 10,
        },
        {
          timestamp: new Date(Date.now() - 28 * 60 * 60 * 1000),
          csvUrl:
            'https://www.stats.govt.nz/assets/Uploads/Business-operations-survey/Business-operations-survey-2023/Download-data/business-operations-survey-2023-CSV-notes.xlsx',
          resultsCount: 20,
        },
        {
          timestamp: new Date(Date.now() - 5 * 24 * 60 * 60 * 1000),
          csvUrl:
            'https://www.stats.govt.nz/assets/Uploads/Business-operations-survey/Business-operations-survey-2023/Download-data/business-operations-survey-2023-CSV-notes.xlsx',
          resultsCount: 23,
        },
      ];

      loading.value = false;
    }, 1500);
  });
</script>

<template>
  <Dialog
    v-model:visible="visible"
    modal
    :header="t('previousResults.title')"
    :style="{ width: '50vw' }"
  >
    <div class="p-4">
      <div v-if="loading" class="flex justify-center items-center h-48">
        <ProgressSpinner />
      </div>
      <div v-else-if="previousResultFiles.length === 0">
        <p>{{ t('previousResults.noResults') }}</p>
      </div>
      <div v-else>
        <div class="rounded-lg bg-gray-800 shadow-lg p-2">
          <DataTable :value="previousResultFiles" class="p-datatable-sm">
            <Column :header="t('previousResults.date')">
              <template #body="slotProps">
                <div v-tooltip.left="formatDate(slotProps.data.timestamp)">
                  {{ formatDistance(slotProps.data.timestamp) }}
                </div>
              </template>
            </Column>
            <Column field="resultsCount" :header="t('previousResults.resultsCount')"></Column>
            <Column :header="t('previousResults.download')">
              <template #body="slotProps">
                <a :href="slotProps.data.csvUrl" download>
                  <Button icon="pi pi-download" class="p-button-rounded p-button-text" />
                </a>
              </template>
            </Column>
          </DataTable>
        </div>
      </div>
    </div>
  </Dialog>
</template>
