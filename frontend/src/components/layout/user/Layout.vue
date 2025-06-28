<script setup>
  import { ref } from 'vue';
  import Sidebar from './Sidebar.vue';
  import Toolbar from './Toolbar.vue';

  const { title } = defineProps({
    title: {
      type: String,
      required: true,
    },
  });

  const sidebarOpen = ref(true);

  const toggleSidebar = () => {
    sidebarOpen.value = !sidebarOpen.value;
  };
</script>

<template>
  <div class="min-h-screen bg-gray-900 text-white flex w-full">
    <!-- Sidebar -->
    <sidebar :sidebar-open="sidebarOpen"></sidebar>

    <!-- Main Content -->
    <div class="transition-all duration-300 ease-in-out flex-grow-3">
      <!-- Top Toolbar -->
      <toolbar :title="title" @toggle-sidebar="toggleSidebar"></toolbar>

      <!-- Main content -->
      <slot></slot>
    </div>
  </div>
</template>

<style>
  /* Custom scrollbar for webkit browsers */
  ::-webkit-scrollbar {
    width: 6px;
  }

  ::-webkit-scrollbar-track {
    background: #374151;
  }

  ::-webkit-scrollbar-thumb {
    background: #6b7280;
    border-radius: 3px;
  }

  ::-webkit-scrollbar-thumb:hover {
    background: #9ca3af;
  }

  /* Smooth transitions */
  * {
    transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    transition-duration: 150ms;
  }
</style>
