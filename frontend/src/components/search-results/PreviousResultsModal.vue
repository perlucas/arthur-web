<script setup>
  import { Dialog } from 'primevue';
  import { ref, onMounted } from 'vue';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  import Button from 'primevue/button';
  import ProgressSpinner from 'primevue/progressspinner';
  import { formatDistanceToNow } from 'date-fns';

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

  const formatDate = (date) => {
    return formatDistanceToNow(new Date(date), { addSuffix: true });
  };
</script>

<template>
  <Dialog v-model:visible="visible" modal header="Previous Results" :style="{ width: '50vw' }">
    <div class="p-4">
      <div v-if="loading" class="flex justify-center items-center h-48">
        <ProgressSpinner />
      </div>
      <div v-else-if="previousResultFiles.length === 0">
        <p>No previous results found.</p>
      </div>
      <div v-else>
        <div class="rounded-lg bg-gray-800 shadow-lg p-2">
          <DataTable :value="previousResultFiles" class="p-datatable-sm">
            <Column header="Date">
              <template #body="slotProps">
                {{ formatDate(slotProps.data.timestamp) }}
              </template>
            </Column>
            <Column field="resultsCount" header="# Results"></Column>
            <Column header="Download">
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
