<script setup>
  import Layout from '../layout/user/Layout.vue';
  import { ref } from 'vue';
  import SearchModal from './SearchModal.vue';
  import { useRouter } from 'vue-router';
  import { useI18n } from 'vue-i18n';
  import { useDateFns } from '@/composables/useDateFns';

  const router = useRouter();

  const { t } = useI18n();
  const { formatDistance } = useDateFns();

  const jobSearches = ref([
    {
      id: 1,
      name: 'Senior Frontend Developer',
      lastUpdated: new Date(Date.now() - 2 * 60 * 60 * 1000),
      isActive: true,
      resultsCount: 24,
      location: 'San Francisco, CA',
      includeTitleTerms: ['Senior', 'Frontend', 'Developer'],
      excludeTitleTerms: [],
      includeKeywords: ['React', 'Vue'],
      excludeKeywords: ['Angular'],
      emailNotifications: true,
    },
    {
      id: 2,
      name: 'React Developer Remote',
      lastUpdated: new Date(Date.now() - 24 * 60 * 60 * 1000),
      isActive: true,
      resultsCount: 18,
      location: 'Remote',
      includeTitleTerms: ['React', 'Developer'],
      excludeTitleTerms: ['Manager'],
      includeKeywords: ['TypeScript', 'Next.js'],
      excludeKeywords: [],
      emailNotifications: true,
    },
    {
      id: 3,
      name: 'UI/UX Designer',
      lastUpdated: new Date(Date.now() - 3 * 24 * 60 * 60 * 1000),
      isActive: false,
      resultsCount: 12,
      location: 'New York, NY',
      includeTitleTerms: ['UI/UX', 'Designer'],
      excludeTitleTerms: [],
      includeKeywords: ['Figma', 'Sketch'],
      excludeKeywords: [],
      emailNotifications: false,
    },
    {
      id: 4,
      name: 'Full Stack Engineer',
      lastUpdated: new Date(Date.now() - 5 * 60 * 60 * 1000),
      isActive: true,
      resultsCount: 31,
      location: 'Austin, TX',
      includeTitleTerms: ['Full Stack', 'Engineer'],
      excludeTitleTerms: [],
      includeKeywords: ['Node.js', 'Python', 'AWS'],
      excludeKeywords: [],
      emailNotifications: true,
    },
    {
      id: 5,
      name: 'Product Manager',
      lastUpdated: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000),
      isActive: false,
      resultsCount: 8,
      location: 'Seattle, WA',
      includeTitleTerms: ['Product Manager'],
      excludeTitleTerms: [],
      includeKeywords: ['Agile', 'Scrum'],
      excludeKeywords: [],
      emailNotifications: false,
    },
    {
      id: 6,
      name: 'DevOps Engineer',
      lastUpdated: new Date(Date.now() - 6 * 60 * 60 * 1000),
      isActive: true,
      resultsCount: 15,
      location: 'Denver, CO',
      includeTitleTerms: ['DevOps', 'Engineer'],
      excludeTitleTerms: [],
      includeKeywords: ['Kubernetes', 'Docker', 'CI/CD'],
      excludeKeywords: [],
      emailNotifications: true,
    },
  ]);

  const editingSearchId = ref(null);

  const toggleSearch = (searchId) => {
    const search = jobSearches.value.find((s) => s.id === searchId);
    if (search) {
      console.log(`Job search "${search.name}" ${search.isActive ? 'activated' : 'paused'}`);
    }
  };

  const onViewSearchResults = (search) => {
    router.push(`/show-results/${search.id}`);
  };

  const searchModalVisible = ref(false);
  const searchModalMode = ref('create');
  const searchModalInitialData = ref(null);

  const onCreateSearch = () => {
    searchModalMode.value = 'create';
    searchModalInitialData.value = null;
    editingSearchId.value = null;
    searchModalVisible.value = true;
  };

  const onEditSearch = (search) => {
    searchModalMode.value = 'edit';
    editingSearchId.value = search.id;
    const { id: _id, lastUpdated: _lastUpdated, resultsCount: _resultsCount, ...formData } = search;
    searchModalInitialData.value = formData;
    searchModalVisible.value = true;
  };

  const handleSearchCreated = (newSearch) => {
    jobSearches.value.push(newSearch);
    console.log('Search created:', newSearch);
  };

  const handleSearchSaved = (updatedSearchData) => {
    const index = jobSearches.value.findIndex((s) => s.id === editingSearchId.value);
    if (index !== -1) {
      jobSearches.value[index] = {
        ...jobSearches.value[index],
        ...updatedSearchData,
        lastUpdated: new Date(),
      };
      console.log('Search saved:', jobSearches.value[index]);
    }
    editingSearchId.value = null;
  };

  const handleSearchDeleted = () => {
    if (editingSearchId.value === null) return;
    jobSearches.value = jobSearches.value.filter((s) => s.id !== editingSearchId.value);
    console.log('Search deleted:', editingSearchId.value);
    editingSearchId.value = null;
  };
</script>

<template>
  <layout :title="t('dashboard.title')">
    <!-- Dashboard Content -->
    <main class="p-6">
      <div class="mb-6">
        <div class="flex items-center justify-between">
          <div>
            <h1 class="text-2xl font-bold text-white">{{ $t('dashboard.yourJobSearches') }}</h1>
            <p class="text-gray-400 mt-1">{{ $t('dashboard.manageCampaigns') }}</p>
          </div>
          <button
            class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg flex items-center transition-colors duration-200"
            @click="onCreateSearch"
          >
            <i class="pi pi-plus mr-2" />
            {{ $t('dashboard.newSearch') }}
          </button>
        </div>
      </div>

      <!-- Job Search Cards Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="search in jobSearches"
          :key="search.id"
          class="bg-gray-800 rounded-lg shadow-lg border border-gray-700 hover:border-gray-600 transition-all duration-200"
        >
          <div class="p-6">
            <!-- Header with title and status -->
            <div class="flex items-start justify-between mb-4">
              <div class="flex-1">
                <h3 class="text-lg font-semibold text-white mb-2">
                  {{ search.name }}
                </h3>
                <div class="flex items-center text-sm text-gray-400">
                  <i class="pi pi-calendar mr-2" />
                  {{ $t('dashboard.updated') }}
                  {{ formatDistance(search.lastUpdated) }}
                </div>
              </div>
              <div class="flex items-center ml-4">
                <div class="flex items-center">
                  <span class="text-sm text-gray-400 mr-3">{{
                    search.isActive ? $t('dashboard.active') : $t('dashboard.paused')
                  }}</span>
                  <label class="relative inline-flex items-center cursor-pointer">
                    <input
                      v-model="search.isActive"
                      type="checkbox"
                      class="sr-only peer"
                      @change="toggleSearch(search.id)"
                    />
                    <div
                      class="w-11 h-6 bg-gray-600 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"
                    />
                  </label>
                </div>
              </div>
            </div>

            <!-- Status indicator -->
            <div class="flex items-center mb-4">
              <div class="flex items-center">
                <div
                  :class="search.isActive ? 'bg-green-500' : 'bg-gray-500'"
                  class="w-3 h-3 rounded-full mr-2"
                />
                <span class="text-sm" :class="search.isActive ? 'text-green-400' : 'text-gray-400'">
                  {{ search.isActive ? $t('dashboard.monitoring') : $t('dashboard.paused') }}
                </span>
              </div>
              <div class="ml-auto text-sm text-gray-400">
                {{ search.resultsCount }} {{ $t('dashboard.results') }}
              </div>
            </div>

            <!-- Search details -->
            <div class="space-y-2 mb-4">
              <div class="flex items-center text-sm text-gray-400">
                <i class="pi pi-map-marker mr-2" />
                {{ search.location }}
              </div>
            </div>

            <!-- Action buttons -->
            <div class="flex space-x-2">
              <button
                class="flex-1 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md text-sm font-medium transition-colors duration-200 flex items-center justify-center"
                @click="onViewSearchResults(search)"
              >
                <i class="pi pi-eye mr-2" />
                {{ $t('dashboard.viewResults') }}
              </button>
              <button
                class="px-3 py-2 bg-gray-700 hover:bg-gray-600 text-gray-300 rounded-md transition-colors duration-200 cursor-pointer"
                @click="onEditSearch(search)"
              >
                <i class="pi pi-cog" />
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty state (when no searches) -->
      <div v-if="jobSearches.length === 0" class="text-center py-12">
        <div class="bg-gray-800 rounded-lg p-8 max-w-md mx-auto">
          <i class="pi pi-search text-4xl text-gray-500 mb-4" />
          <h3 class="text-xl font-semibold text-white mb-2">{{ $t('dashboard.noSearchesYet') }}</h3>
          <p class="text-gray-400 mb-4">
            {{ $t('dashboard.createFirstSearch') }}
          </p>
          <button
            class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg"
            @click="onCreateSearch"
          >
            {{ $t('dashboard.createJobSearch') }}
          </button>
        </div>
      </div>
    </main>

    <SearchModal
      v-model:visible="searchModalVisible"
      :mode="searchModalMode"
      :initial-data="searchModalInitialData"
      @search-created="handleSearchCreated"
      @search-saved="handleSearchSaved"
      @search-deleted="handleSearchDeleted"
    />
  </layout>
</template>
