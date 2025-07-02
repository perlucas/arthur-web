<script setup>
  import { useRoute } from 'vue-router';
  import { useI18n } from 'vue-i18n';
  import { Badge } from 'primevue';
  import { ref } from 'vue';

  const { t } = useI18n();

  const { sidebarOpen } = defineProps({
    sidebarOpen: Boolean,
  });

  const route = useRoute();

  const navbarItems = [
    {
      title: t('sidebar.jobSearches'),
      icon: 'pi-search',
      path: '/dashboard',
    },
    {
      title: t('sidebar.notifications'),
      icon: 'pi-bell',
      path: '/notifications',
    },
    {
      title: t('sidebar.payments'),
      icon: 'pi-wallet',
      path: '/payments',
    },
  ];

  /**
   *
   * @param path {string}
   */
  const isCurrentLinkActive = (path) => path.startsWith(route.path);

  const colors = {
    sidebarBg: 'bg-gray-800',
    logoBg: 'bg-gray-900',
    activeLinkBg: 'bg-gray-700',
    activeLinkText: 'text-white',
    regularLinkText: 'text-gray-300',
  };

  const notifications = ref(2); // TODO: Replace with actual notifications count
</script>

<template>
  <div
    class="inset-y-0 left-0 min-w-64 z-50 shadow-lg transform transition-transform duration-300 ease-in-out"
    :class="{ hidden: !sidebarOpen, [colors.sidebarBg]: true }"
  >
    <!-- Logo -->
    <div class="flex items-center justify-center h-16" :class="{ [colors.logoBg]: true }">
      <h1 class="text-xl font-bold text-blue-400">{{ t('sidebar.brandName') }}</h1>
    </div>

    <!-- Navbar items list -->
    <nav class="mt-8">
      <div class="px-4 space-y-2">
        <RouterLink
          v-for="item in navbarItems"
          :key="item.path"
          class="flex items-center px-4 py-3 rounded-lg transition-colors duration-200"
          :class="{
            [colors.regularLinkText]: true,
            [`hover:${colors.activeLinkBg}`]: true,
            [`hover:${colors.activeLinkText}`]: true,
            [colors.activeLinkText]: isCurrentLinkActive(item.path),
            [colors.activeLinkBg]: isCurrentLinkActive(item.path),
          }"
          :to="item.path"
        >
          <i :class="`pi ${item.icon} mr-3`"></i>
          {{ item.title }}

          <Badge
            v-if="item.path === '/notifications' && notifications > 0"
            :value="notifications"
            severity="info"
            class="p-1 ml-2"
          ></Badge>
        </RouterLink>
      </div>
    </nav>
  </div>
</template>
