<script setup>
  import { ref } from 'vue';
  import Dialog from 'primevue/dialog';
  import InputText from 'primevue/inputtext';
  import { useI18n } from 'vue-i18n';

  const { t } = useI18n();
  const visible = defineModel({ default: false, type: Boolean });
  const emit = defineEmits(['close']);

  const currentPassword = ref('');
  const newPassword = ref('');
  const confirmPassword = ref('');

  const closeModal = () => {
    visible.value = false;
    emit('close');
  };

  const handleConfirm = () => {
    console.log('Confirming password change...');
    // Here you would add validation and the API call
    closeModal();
  };
</script>

<template>
  <Dialog
    v-model:visible="visible"
    modal
    :header="t('changePasswordModal.title')"
    :style="{ width: '90%', maxWidth: '500px' }"
    @update:visible="
      (v) => {
        visible = v;
        if (!v) closeModal();
      }
    "
  >
    <div class="p-4 text-white">
      <div class="space-y-6">
        <div>
          <label for="current-password" class="block text-sm font-medium text-gray-300 mb-2">
            {{ t('changePasswordModal.currentPassword') }}
          </label>
          <InputText
            id="current-password"
            v-model="currentPassword"
            type="password"
            class="w-full bg-gray-700 border-gray-600 text-white"
          />
        </div>
        <div>
          <label for="new-password" class="block text-sm font-medium text-gray-300 mb-2">
            {{ t('changePasswordModal.newPassword') }}
          </label>
          <InputText
            id="new-password"
            v-model="newPassword"
            type="password"
            class="w-full bg-gray-700 border-gray-600 text-white"
          />
        </div>
        <div>
          <label for="confirm-password" class="block text-sm font-medium text-gray-300 mb-2">
            {{ t('changePasswordModal.confirmNewPassword') }}
          </label>
          <InputText
            id="confirm-password"
            v-model="confirmPassword"
            type="password"
            class="w-full bg-gray-700 border-gray-600 text-white"
          />
        </div>
      </div>
    </div>
    <template #footer>
      <div class="px-4 flex justify-end space-x-2">
        <button
          type="button"
          @click="closeModal"
          class="px-6 py-2 bg-gray-600 hover:bg-gray-700 rounded-md font-bold cursor-pointer"
        >
          {{ t('changePasswordModal.cancel') }}
        </button>
        <button
          type="button"
          @click="handleConfirm"
          class="px-6 py-2 bg-blue-600 hover:bg-blue-700 rounded-md font-bold cursor-pointer"
        >
          {{ t('changePasswordModal.confirm') }}
        </button>
      </div>
    </template>
  </Dialog>
</template>

<style scoped>
  :deep(.p-dialog-header) {
    background-color: #1f2937; /* bg-gray-800 */
    color: white;
    border-bottom: 1px solid #374151; /* border-gray-700 */
  }
  :deep(.p-dialog-title) {
    font-size: 1.25rem;
    font-weight: 600;
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
  :deep(.p-inputtext) {
    padding: 0.75rem;
  }
</style>
