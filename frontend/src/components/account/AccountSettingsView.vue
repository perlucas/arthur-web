<script setup>
  import Layout from '../layout/user/Layout.vue';
  import { ref } from 'vue';
  import { useI18n } from 'vue-i18n';
  import { Select } from 'primevue';
  import { useDateFns } from '@/composables/useDateFns';
  import ChangePasswordModal from './ChangePasswordModal.vue';
  import PricingInfoModal from './PricingInfoModal.vue';

  const { t } = useI18n();
  const { formatDate } = useDateFns();

  const emailNotifications = ref(true);
  const selectedLanguage = ref('en');

  const subscription = ref({
    plan: 'demo',
    expires: new Date('2024-08-08'),
  });

  const handleUpdateSettings = () => {
    console.log('Updating general settings...');
  };

  const changePasswordModalVisible = ref(false);

  const handleChangePassword = () => {
    changePasswordModalVisible.value = true;
  };

  const handleUpgradePlan = () => {
    console.log('Upgrading plan...');
  };

  const handleRenewSubscription = () => {
    console.log('Renewing subscription...');
  };

  const handleDeleteAccount = () => {
    console.log('Deleting account...');
  };

  const pricingModalOpen = ref(false);
</script>

<template>
  <Layout :title="t('accountSettings.title')">
    <main class="p-6">
      <!-- Header -->
      <div class="mb-6">
        <h1 class="text-2xl font-bold text-white">{{ t('accountSettings.title') }}</h1>
        <p class="text-gray-400 mt-1">{{ t('accountSettings.subtitle') }}</p>
      </div>

      <div class="grid grid-cols-1 gap-6">
        <!-- General Settings -->
        <div class="bg-gray-800 rounded-lg shadow-lg border border-gray-700 p-6">
          <h2 class="text-xl font-semibold text-white mb-4">
            {{ t('accountSettings.general.title') }}
          </h2>
          <div class="space-y-4 flex justify-between">
            <!-- Email Notifications -->
            <div class="flex items-center justify-between">
              <div class="mr-4">
                <label for="email-notifications" class="font-medium text-white">
                  {{ t('accountSettings.general.emailNotifications.label') }}
                </label>
                <p class="text-sm text-gray-400">
                  {{ t('accountSettings.general.emailNotifications.description') }}
                </p>
              </div>
              <label class="relative inline-flex items-center cursor-pointer">
                <input
                  v-model="emailNotifications"
                  type="checkbox"
                  id="email-notifications"
                  class="sr-only peer"
                />
                <div
                  class="w-11 h-6 bg-gray-600 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"
                ></div>
              </label>
            </div>

            <!-- Language Selection -->
            <div class="flex items-center justify-between">
              <div class="mr-4">
                <label for="language" class="font-medium text-white">{{
                  t('accountSettings.general.language.label')
                }}</label>
                <p class="text-sm text-gray-400">
                  {{ t('accountSettings.general.language.description') }}
                </p>
              </div>

              <Select
                v-model="selectedLanguage"
                id="language"
                option-label="label"
                option-value="value"
                :options="[
                  { label: 'English', value: 'en' },
                  { label: 'Spanish', value: 'es' },
                ]"
                class="!rounded-md"
              >
              </Select>
            </div>
          </div>
          <div class="mt-6 text-right">
            <button
              @click="handleUpdateSettings"
              class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors duration-200"
            >
              {{ t('accountSettings.general.saveChanges') }}
            </button>
          </div>
        </div>

        <!-- Security Settings -->
        <div class="bg-gray-800 rounded-lg shadow-lg border border-gray-700 p-6">
          <h2 class="text-xl font-semibold text-white mb-4">
            {{ t('accountSettings.security.title') }}
          </h2>
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <div>
                <label for="new-password" class="font-medium text-white">{{
                  t('accountSettings.security.newPassword.label')
                }}</label>
                <p class="text-sm text-gray-400">
                  {{ t('accountSettings.security.newPassword.description') }}
                </p>
              </div>
              <div class="flex items-center space-x-2">
                <button
                  @click="handleChangePassword"
                  class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors duration-200"
                >
                  {{ t('accountSettings.security.changePassword') }}
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Subscription Status -->
        <div class="bg-gray-800 rounded-lg shadow-lg border border-gray-700 p-6">
          <h2 class="text-xl font-semibold text-white mb-4">
            {{ t('accountSettings.subscription.title') }}
          </h2>
          <div class="flex justify-between items-center">
            <div class="flex items-center mb-4 space-x-6">
              <div>
                <p class="text-gray-400">{{ t('accountSettings.subscription.currentPlan') }}</p>
                <p class="text-2xl font-bold text-white">
                  {{ t(`accountSettings.subscription.plans.${subscription.plan}`) }}
                </p>
              </div>
              <div>
                <p class="text-gray-400">{{ t('accountSettings.subscription.expiresOn') }}</p>
                <p class="text-2xl font-bold text-white capitalize">
                  {{ formatDate(subscription.expires, 'MMM d, yyyy') }}
                </p>
              </div>
            </div>

            <div class="text-center">
              <button
                v-if="subscription.plan === 'demo'"
                @click="handleUpgradePlan"
                class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-lg transition-colors duration-200 flex items-center"
              >
                <i class="pi pi-arrow-up mr-2"></i>
                {{ t('accountSettings.subscription.upgradePlan') }}
              </button>
              <button
                v-else
                @click="handleRenewSubscription"
                class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors duration-200 flex items-center"
              >
                <i class="pi pi-refresh mr-2"></i>
                {{ t('accountSettings.subscription.renewSubscription') }}
              </button>
              <p class="text-gray-400 text-sm mt-2 cursor-pointer hover:text-gray-300">
                <a @click="pricingModalOpen = true">
                  {{ t('accountSettings.subscription.pricingInfo') }}
                </a>
              </p>
            </div>
          </div>
        </div>

        <!-- Delete Account -->
        <div class="bg-gray-800 rounded-lg shadow-lg border border-gray-700 p-6">
          <h2 class="text-xl font-semibold text-white mb-4">
            {{ t('accountSettings.deleteAccount.title') }}
          </h2>
          <div class="flex items-center justify-between">
            <div>
              <p class="font-medium text-white">{{ t('accountSettings.deleteAccount.label') }}</p>
              <p class="text-sm text-gray-400">
                {{ t('accountSettings.deleteAccount.description') }}
              </p>
            </div>
            <button
              @click="handleDeleteAccount"
              class="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-lg transition-colors duration-200 flex items-center"
            >
              <i class="pi pi-trash mr-2"></i>
              {{ t('accountSettings.deleteAccount.deleteButton') }}
            </button>
          </div>
        </div>
      </div>
    </main>
  </Layout>
  <ChangePasswordModal
    :visible="changePasswordModalVisible"
    @close="changePasswordModalVisible = false"
  />
  <PricingInfoModal v-model="pricingModalOpen" @close="pricingModalOpen = false" />
</template>
