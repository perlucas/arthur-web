<script setup>
  import { AutoComplete, Button, Checkbox, Dialog, InputText } from 'primevue';
  import { ref, reactive, watch } from 'vue';
  import { z } from 'zod';
  import ChipsInput from './ChipsInput.vue';

  // Model
  const visible = defineModel({ default: false, type: Boolean });

  const props = defineProps({
    mode: {
      type: String, // 'create' or 'edit'
      required: true,
      validator: (value) => ['create', 'edit'].includes(value),
    },
    initialData: {
      type: Object,
      default: null,
    },
  });

  // Exposed
  defineExpose({
    open: () => {
      console.log('opened!');
      visible.value = true;
    },
  });

  // Emits
  const emit = defineEmits(['update:visible', 'search-created', 'search-saved', 'search-deleted']);

  // Form data
  const formData = reactive({
    searchName: '',
    includeTitleTerms: [],
    excludeTitleTerms: [],
    includeKeywords: [],
    excludeKeywords: [],
    location: '',
    emailNotifications: true,
    isActive: true, // Include isActive for both modes, default to true for create
  });

  // Form errors
  const errors = ref({});

  // Loading state
  const loading = ref(false);

  watch(
    () => [props.mode, props.initialData],
    ([mode, initialData]) => {
      if (mode === 'edit' && initialData) {
        Object.assign(formData, initialData);
      } else {
        // Reset for 'create' mode or if initialData is null
        formData.searchName = '';
        formData.includeTitleTerms = [];
        formData.excludeTitleTerms = [];
        formData.includeKeywords = [];
        formData.excludeKeywords = [];
        formData.location = '';
        formData.emailNotifications = true;
        formData.isActive = true;
      }
      errors.value = {}; // Clear errors on mode/data change
    },
    { immediate: true },
  );

  // Location autocomplete
  const locations = [
    'New York, NY',
    'San Francisco, CA',
    'Los Angeles, CA',
    'Chicago, IL',
    'Austin, TX',
    'Seattle, WA',
    'Boston, MA',
    'Denver, CO',
    'Atlanta, GA',
    'Miami, FL',
    'Portland, OR',
    'Washington, DC',
    'Dallas, TX',
    'Phoenix, AZ',
    'Remote',
    'Hybrid - San Francisco, CA',
    'Hybrid - New York, NY',
    'Hybrid - Austin, TX',
  ];

  const filteredLocations = ref([]);

  const searchLocation = (event) => {
    const query = event.query.toLowerCase();
    filteredLocations.value = locations.filter((location) =>
      location.toLowerCase().includes(query),
    );
  };

  // Validation schema
  const schema = z.object({
    searchName: z.string().min(3, 'Search name must be at least 3 characters'),
    location: z
      .string()
      .min(1, 'Location is required')
      .refine((val) => locations.includes(val), {
        message: 'Please select a valid location from the list.',
      }),
    includeTitleTerms: z
      .array(z.string())
      .min(1, 'At least one include term is required for Job Title'),
  });

  // Form validation
  const validateForm = () => {
    try {
      schema.parse({
        searchName: formData.searchName,
        location: formData.location,
        includeTitleTerms: formData.includeTitleTerms,
      });
      errors.value = {};
      return true;
    } catch (error) {
      errors.value = {};
      error.errors.forEach((err) => {
        errors.value[err.path[0]] = err.message;
      });
      return false;
    }
  };

  // Form submission
  const submitForm = async () => {
    if (!validateForm()) {
      return;
    }

    loading.value = true;

    try {
      // Simulate API call
      await new Promise((resolve) => setTimeout(resolve, 1000));

      if (props.mode === 'create') {
        const newSearch = {
          id: Date.now(),
          title: formData.searchName,
          lastUpdated: new Date(),
          isActive: true,
          resultsCount: 0,
          location: formData.location,
          jobType: 'Full-time', // Example default
          sources: ['LinkedIn', 'Indeed'], // Example default
          ...formData, // Spread current form data
        };
        emit('search-created', newSearch);
      } else {
        // mode === 'edit'
        emit('search-saved', {
          ...formData,
          lastUpdated: new Date(), // Update last updated on save
        });
      }
      resetForm();
      closeModal();
    } catch (error) {
      console.error(`Error ${props.mode === 'create' ? 'creating' : 'saving'} search:`, error);
    } finally {
      loading.value = false;
    }
  };

  // Reset form
  const resetForm = () => {
    formData.searchName = '';
    formData.includeTitleTerms = [];
    formData.excludeTitleTerms = [];
    formData.includeKeywords = [];
    formData.excludeKeywords = [];
    formData.location = '';
    formData.emailNotifications = true;
    formData.isActive = true;

    errors.value = {};
  };

  // Close modal
  const closeModal = () => {
    visible.value = false;
    emit('update:visible', visible.value);
  };

  const deleteSearch = () => {
    emit('search-deleted', props.initialData.id); // Emit ID of deleted search
    closeModal();
  };
</script>

<template>
  <Dialog
    :visible="visible"
    :modal="true"
    :closable="true"
    :dismissable-mask="true"
    :header="mode === 'create' ? 'Create New Job Search' : 'Edit Job Search'"
    :style="{ width: '90%', maxWidth: '700px' }"
    class="custom-dialog"
    @update:visible="
      (v) => {
        visible = v;
        emit('update:visible', visible);
      }
    "
  >
    <div class="p-6">
      <form @submit.prevent="submitForm">
        <!-- Search Name -->
        <div class="mb-6">
          <label for="searchName" class="block text-sm font-medium text-gray-300 mb-2">
            Search Name <span class="text-red-500">*</span>
          </label>
          <InputText
            id="searchName"
            v-model="formData.searchName"
            placeholder="Enter a name for this search"
            class="w-full"
            :class="{ 'p-invalid': errors.searchName }"
          />
          <small v-if="errors.searchName" class="p-error block mt-1">
            {{ errors.searchName }}
          </small>
        </div>

        <!-- Location Section -->
        <div class="mb-6">
          <label for="location" class="block text-sm font-medium text-gray-300 mb-2">
            Location <span class="text-red-500">*</span>
          </label>
          <AutoComplete
            id="location"
            v-model="formData.location"
            :suggestions="filteredLocations"
            @complete="searchLocation"
            placeholder="Search for a location"
            class="w-full"
            input-class="w-full"
            :class="{ 'p-invalid': errors.location }"
          />
          <small v-if="errors.location" class="p-error block mt-1">
            {{ errors.location }}
          </small>
        </div>

        <!-- Title Section -->
        <div class="mb-6">
          <div class="flex items-center mb-4">
            <h3 class="text-lg font-medium text-blue-400 mr-2">Job Title</h3>
            <i
              class="pi pi-info-circle text-blue-300 cursor-pointer"
              v-tooltip="
                'These are the primary search terms used when looking up job postings, include/exclude up to 3 terms.'
              "
            ></i>
          </div>

          <div class="mb-4">
            <label for="includeTitles" class="block text-sm font-medium text-gray-300 mb-2">
              Include these words in the title <span class="text-red-500">*</span>
            </label>
            <ChipsInput
              id="includeTitles"
              v-model="formData.includeTitleTerms"
              chip-color="bg-blue-600"
              chip-text="text-white"
              chip-remove="text-blue-200 hover:text-white"
              :max-items="3"
            />
            <small v-if="errors.includeTitleTerms" class="p-error block mt-1">
              {{ errors.includeTitleTerms }}
            </small>
          </div>

          <div>
            <label for="excludeTitles" class="block text-sm font-medium text-gray-300 mb-2">
              Exclude these words from the title
            </label>
            <ChipsInput
              id="excludeTitles"
              v-model="formData.excludeTitleTerms"
              chip-color="bg-red-500"
              chip-text="text-white"
              chip-remove="text-red-200 hover:text-white"
              :max-items="3"
            />
          </div>
        </div>

        <!-- Keywords Section -->
        <div class="mb-6">
          <div class="flex items-center mb-4">
            <h3 class="text-lg font-medium text-blue-400 mr-2">Job Description Keywords</h3>
            <i
              class="pi pi-info-circle text-blue-300 cursor-pointer"
              v-tooltip="
                'Use these terms to make your search more specific by including/excluding keywords from the job posting\'s description'
              "
            ></i>
          </div>

          <div class="mb-4">
            <label for="includeKeywords" class="block text-sm font-medium text-gray-300 mb-2">
              Include these keywords in the description
            </label>
            <ChipsInput
              id="includeKeywords"
              v-model="formData.includeKeywords"
              chip-color="bg-blue-600"
              chip-text="text-white"
              chip-remove="text-blue-200 hover:text-white"
              :max-items="3"
            />
          </div>

          <div>
            <label for="excludeKeywords" class="block text-sm font-medium text-gray-300 mb-2">
              Exclude these keywords from the description
            </label>
            <ChipsInput
              id="excludeKeywords"
              v-model="formData.excludeKeywords"
              chip-color="bg-red-500"
              chip-text="text-white"
              chip-remove="text-red-200 hover:text-white"
              :max-items="3"
            />
          </div>
        </div>

        <!-- Email Notifications -->
        <div class="mb-6">
          <div class="flex items-center">
            <Checkbox
              id="notifications"
              v-model="formData.emailNotifications"
              :binary="true"
              class="mr-3"
            />
            <label for="notifications" class="text-sm font-medium text-gray-300 cursor-pointer">
              Send email notifications when new results arrive
            </label>
          </div>
        </div>

        <!-- Form Actions -->
        <div
          class="flex mt-8"
          :class="{ 'justify-between': mode === 'edit', 'justify-end': mode === 'create' }"
        >
          <!-- Status Switch -->
          <div v-if="mode === 'edit'" class="flex items-center mt-2">
            <span class="text-sm text-gray-400 mr-3">{{
              formData.isActive ? 'Active' : 'Paused'
            }}</span>
            <label class="relative inline-flex items-center cursor-pointer">
              <input type="checkbox" v-model="formData.isActive" class="sr-only peer" />
              <div
                class="w-11 h-6 bg-gray-600 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"
              ></div>
            </label>
          </div>

          <div class="flex justify-end space-x-3">
            <Button
              type="button"
              label="Cancel"
              @click="closeModal"
              severity="secondary"
              class="px-6 py-2"
            />
            <Button
              v-if="mode === 'edit'"
              type="button"
              label="Delete"
              @click="deleteSearch"
              severity="danger"
              class="px-6 py-2"
            />
            <Button
              type="submit"
              :label="mode === 'create' ? 'Create Search' : 'Save'"
              class="px-6 py-2"
              severity="primary"
              :loading="loading"
            />
          </div>
        </div>
      </form>
    </div>
  </Dialog>
</template>

<style scoped>
  /* Custom dialog styling to match dashboard theme */

  :deep(.p-dialog-title) {
    color: white;
    font-size: 1.25rem;
    font-weight: 600;
  }

  :deep(.p-dialog-header-close) {
    color: #9ca3af;
    width: 2rem;
    height: 2rem;
  }

  :deep(.p-dialog-header-close:hover) {
    color: white;
    background-color: #374151;
  }

  :deep(.p-dialog-content) {
    background-color: #1f2937;
    color: white;
    padding: 0;
    border-radius: 0 0 0.5rem 0.5rem;
  }

  /* Input styling */
  :deep(.p-inputtext) {
    color: white;
    padding: 0.75rem;
    border-radius: 0.375rem;
  }

  :deep(.p-inputtext:enabled:focus) {
    box-shadow: 0 0 0 1px #3b82f6;
    border-color: #3b82f6;
  }

  :deep(.p-inputtext::placeholder) {
    color: #9ca3af;
  }

  /* AutoComplete styling */
  :deep(.p-autocomplete-input) {
    color: white;
    padding: 0.75rem;
    border-radius: 0.375rem;
  }

  :deep(.p-autocomplete-panel) {
    background-color: #374151;
    border: 1px solid #4b5563;
    border-radius: 0.375rem;
  }

  :deep(.p-autocomplete-item) {
    color: white;
    padding: 0.75rem;
  }

  :deep(.p-autocomplete-item:hover) {
    background-color: #4b5563;
  }

  /* Checkbox styling */
  :deep(.p-checkbox-box) {
    background-color: #374151;
    border: 1px solid #4b5563;
    border-radius: 0.25rem;
    width: 1.25rem;
    height: 1.25rem;
  }

  :deep(.p-checkbox-box.p-highlight) {
    background-color: #3b82f6;
    border-color: #3b82f6;
  }

  :deep(.p-checkbox-icon) {
    color: white;
  }

  /* Button styling */
  :deep(.p-button) {
    border-radius: 0.375rem;
    font-weight: 500;
    padding: 0.5rem 1rem;
    color: white;

    &.p-button.p-button-primary {
      color: white;
      border-color: var(--color-blue-600);
      background-color: var(--color-blue-600);
      &:hover {
        background-color: var(--color-blue-700);
      }
    }

    &.p-button.p-button-secondary {
      background-color: var(--color-gray-600);
      &:hover {
        background-color: var(--color-gray-700);
      }
    }

    &.p-button.p-button-danger {
      color: white;
      border-color: var(--color-red-500);
      background-color: var(--color-red-500);
      &:hover {
        background-color: var(--color-red-600);
      }
    }
  }

  /* Error styling */
  :deep(.p-invalid) {
    border-color: #ef4444 !important;
  }

  .p-error {
    color: #ef4444;
    font-size: 0.875rem;
  }
</style>
