<script setup>
  import { ref } from 'vue';
  import InputText from 'primevue/inputtext';
  import { useI18n } from 'vue-i18n';

  const { t } = useI18n();

  const props = defineProps({
    modelValue: {
      type: Array,
      required: true,
    },
    id: {
      type: String,
      default: () => (Math.random() * 1000).toString(36),
    },
    placeholder: {
      type: String,
      default: '',
    },
    chipColor: {
      type: String,
      default: 'bg-blue-600',
    },
    chipText: {
      type: String,
      default: 'text-white',
    },
    chipRemove: {
      type: String,
      default: 'text-blue-200 hover:text-white',
    },
    maxItems: {
      type: Number,
      default: Infinity,
    },
  });
  const emit = defineEmits(['update:modelValue']);

  const input = ref('');

  const addChip = (event) => {
    if ((event.key === 'Enter' || event.key === ',') && props.modelValue.length < props.maxItems) {
      event.preventDefault();
      if (input.value.trim()) {
        emit('update:modelValue', [...props.modelValue, input.value.trim()]);
        input.value = '';
      }
    }
  };

  const removeChip = (index) => {
    const arr = [...props.modelValue];
    arr.splice(index, 1);
    emit('update:modelValue', arr);
  };
</script>

<template>
  <div>
    <InputText
      :id="id"
      v-model="input"
      :placeholder="placeholder || t('chipsInput.placeholder')"
      class="w-full"
      :disabled="modelValue.length >= maxItems"
      @keydown="addChip"
    />
    <div v-if="modelValue.length > 0" class="flex flex-wrap gap-2 mt-2">
      <span
        v-for="(term, index) in modelValue"
        :key="index"
        class="inline-flex items-center px-3 py-1 rounded-full text-sm"
        :class="[chipColor, chipText]"
      >
        {{ term }}
        <button type="button" class="ml-2" :class="chipRemove" @click="removeChip(index)">
          <i class="pi pi-times mt-1" style="font-size: small"></i>
        </button>
      </span>
    </div>
  </div>
</template>
