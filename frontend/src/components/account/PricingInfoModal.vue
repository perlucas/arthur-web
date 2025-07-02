<script setup>
  import { defineModel, defineEmits } from 'vue';
  import Dialog from 'primevue/dialog';
  import { useI18n } from 'vue-i18n';

  const { t } = useI18n();
  const visible = defineModel({ default: false, type: Boolean });
  const emit = defineEmits(['close']);

  const closeModal = () => {
    visible.value = false;
    emit('close');
  };
</script>

<template>
  <Dialog
    v-model:visible="visible"
    modal
    :header="t('pricingInfoModal.header')"
    :style="{ width: '90%', maxWidth: '900px' }"
    @update:visible="!$event && closeModal()"
  >
    <div class="p-8 bg-gray-900 text-white">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Demo Plan -->
        <div
          class="bg-gray-800 p-6 rounded-xl shadow-lg transform hover:scale-105 transition-transform duration-300"
        >
          <div class="text-center mb-6">
            <h3 class="text-2xl font-bold text-yellow-500 mb-2">
              {{ t('pricingInfoModal.demo.title') }}
            </h3>
            <p class="text-4xl font-bold">{{ t('pricingInfoModal.demo.price') }}</p>
            <p class="text-gray-400">{{ t('pricingInfoModal.demo.subtitle') }}</p>
          </div>
          <ul class="space-y-4 text-gray-300">
            <li>
              <i class="pi pi-calendar-times mr-2 text-yellow-500"></i>
              {{ t('pricingInfoModal.demo.feature1') }}
            </li>
            <li>
              <i class="pi pi-briefcase mr-2 text-yellow-500"></i>
              {{ t('pricingInfoModal.demo.feature2') }}
            </li>
            <li>
              <i class="pi pi-power-off mr-2 text-yellow-500"></i>
              {{ t('pricingInfoModal.demo.feature3') }}
            </li>
            <li>
              <i class="pi pi-times-circle mr-2 text-yellow-500"></i>
              {{ t('pricingInfoModal.demo.feature4') }}
            </li>
          </ul>
        </div>

        <!-- Premium Plan -->
        <div
          class="bg-gray-800 p-6 rounded-xl shadow-lg transform hover:scale-105 transition-transform duration-300"
        >
          <div class="text-center mb-6">
            <h3 class="text-2xl font-bold text-blue-400 mb-2">
              {{ t('pricingInfoModal.premium.title') }}
            </h3>
            <p class="text-4xl font-bold">
              {{ t('pricingInfoModal.premium.price')
              }}<span class="text-lg">{{ t('pricingInfoModal.premium.priceUnit') }}</span>
            </p>
            <p class="text-gray-400">{{ t('pricingInfoModal.premium.subtitle') }}</p>
          </div>
          <ul class="space-y-4 text-gray-300">
            <li>
              <i class="pi pi-calendar-plus mr-2 text-blue-400"></i>
              {{ t('pricingInfoModal.premium.feature1') }}
            </li>
            <li>
              <i class="pi pi-briefcase mr-2 text-blue-400"></i>
              {{ t('pricingInfoModal.premium.feature2') }}
            </li>
            <li>
              <i class="pi pi-power-off mr-2 text-blue-400"></i>
              {{ t('pricingInfoModal.premium.feature3') }}
            </li>
            <li>
              <i class="pi pi-upload mr-2 text-blue-400"></i>
              {{ t('pricingInfoModal.premium.feature4') }}
            </li>
          </ul>
        </div>

        <!-- Custom Plan -->
        <div
          class="bg-gray-800 p-6 rounded-xl shadow-lg transform hover:scale-105 transition-transform duration-300"
        >
          <div class="text-center mb-6">
            <h3 class="text-2xl font-bold text-purple-400 mb-2">
              {{ t('pricingInfoModal.custom.title') }}
            </h3>
            <p class="text-4xl font-bold">{{ t('pricingInfoModal.custom.price') }}</p>
            <p class="text-gray-400">{{ t('pricingInfoModal.custom.subtitle') }}</p>
          </div>
          <ul class="space-y-4 text-gray-300">
            <li>
              <i class="pi pi-cog mr-2 text-purple-400"></i>
              {{ t('pricingInfoModal.custom.feature1') }}
            </li>
            <li>
              <i class="pi pi-briefcase mr-2 text-purple-400"></i>
              {{ t('pricingInfoModal.custom.feature2') }}
            </li>
            <li>
              <i class="pi pi-power-off mr-2 text-purple-400"></i>
              {{ t('pricingInfoModal.custom.feature3') }}
            </li>
            <li>
              <i class="pi pi-cloud-upload mr-2 text-purple-400"></i>
              {{ t('pricingInfoModal.custom.feature4') }}
            </li>
          </ul>
        </div>
      </div>
    </div>
    <template #footer>
      <div class="bg-gray-900 px-8 flex justify-end">
        <button
          type="button"
          @click="closeModal"
          class="px-6 py-2 bg-gray-600 hover:bg-gray-700 rounded-md font-bold cursor-pointer"
        >
          {{ t('pricingInfoModal.closeButton') }}
        </button>
      </div>
    </template>
  </Dialog>
</template>

<style scoped>
  :deep(.p-dialog-header) {
    background-color: #111827; /* bg-gray-900 */
    color: white;
    border-bottom: 1px solid #1f2937; /* border-gray-800 */
  }
  :deep(.p-dialog-title) {
    font-size: 1.5rem;
    font-weight: 700;
  }
  :deep(.p-dialog-header-close) {
    color: #9ca3af; /* text-gray-400 */
  }
  :deep(.p-dialog-header-close:hover) {
    color: white;
  }
  :deep(.p-dialog-content) {
    padding: 0;
  }
  :deep(.p-dialog-footer) {
    padding: 0;
  }
</style>
