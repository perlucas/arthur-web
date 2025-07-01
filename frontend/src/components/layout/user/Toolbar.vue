<script setup>
  import avatarPlaceholder from '@/assets/placeholder.png';
  import { ref, onMounted, onUnmounted } from 'vue';
  import { useI18n } from 'vue-i18n';

  const { t } = useI18n();

  const { title } = defineProps({
    title: {
      type: String,
      required: true,
    },
  });

  const userMenuOpen = ref(false);

  const toggleUserMenu = () => {
    userMenuOpen.value = !userMenuOpen.value;
  };

  const emit = defineEmits(['toggle-sidebar']);

  const colors = {
    toolbarBg: 'bg-gray-800',
    titleText: 'text-white',
    userMenuBg: 'bg-gray-700',
    userMenuLinkText: 'text-gray-300',
    userMenuLinkHoverBg: 'bg-gray-600',
    userMenuLinkHoverText: 'text-white',
  };

  // Close user menu when clicking outside
  const handleClickOutside = (event) => {
    if (userMenuOpen.value && !event.target.closest('.relative')) {
      userMenuOpen.value = false;
    }
  };

  onMounted(() => {
    document.addEventListener('click', handleClickOutside);
  });

  onUnmounted(() => {
    document.removeEventListener('click', handleClickOutside);
  });
</script>

<template>
  <header class="shadow-sm" :class="{ [colors.toolbarBg]: true }">
    <div class="flex items-center justify-between px-6 py-4">
      <div class="flex items-center">
        <button
          class="text-gray-400 hover:text-white focus:outline-none focus:text-white mr-4"
          @click="emit('toggle-sidebar')"
        >
          <i class="pi pi-bars text-xl"></i>
        </button>
        <h2 class="text-xl font-semibold" :class="{ [colors.titleText]: true }">{{ title }}</h2>
      </div>

      <div class="flex items-center space-x-4">
        <!-- User Menu -->
        <div class="relative">
          <button
            class="flex items-center text-gray-400 hover:text-white focus:outline-none"
            @click="toggleUserMenu"
          >
            <img
              class="h-8 w-8 rounded-full mr-2"
              :src="avatarPlaceholder"
              :alt="t('toolbar.userAvatarAlt')"
              width="32px"
              height="32px"
            />
            <span class="text-sm font-medium">John Doe</span>
            <i
              class="pi ml-2 text-xs"
              :class="{ 'pi-chevron-down': userMenuOpen, 'pi-chevron-left': !userMenuOpen }"
            ></i>
          </button>

          <div
            v-if="userMenuOpen"
            class="absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 z-50"
            :class="{ [colors.userMenuBg]: true }"
          >
            <RouterLink
              to="/settings"
              class="block px-4 py-2 text-sm"
              :class="{
                [colors.userMenuLinkText]: true,
                [`hover:${colors.userMenuLinkHoverBg}`]: true,
                [`hover:${colors.userMenuLinkHoverText}`]: true,
              }"
            >
              <i class="pi pi-user mr-2"></i>{{ t('toolbar.accountSettings') }}
            </RouterLink>
            <RouterLink
              to="/payments"
              class="block px-4 py-2 text-sm"
              :class="{
                [colors.userMenuLinkText]: true,
                [`hover:${colors.userMenuLinkHoverBg}`]: true,
                [`hover:${colors.userMenuLinkHoverText}`]: true,
              }"
            >
              <i class="pi pi-wallet mr-2"></i>{{ t('toolbar.payments') }}
            </RouterLink>
            <hr class="border-gray-600 my-1" />
            <RouterLink
              to="/signout"
              class="block px-4 py-2 text-sm"
              :class="{
                [colors.userMenuLinkText]: true,
                [`hover:${colors.userMenuLinkHoverBg}`]: true,
                [`hover:${colors.userMenuLinkHoverText}`]: true,
              }"
            >
              <i class="pi pi-sign-out mr-2"></i>{{ t('toolbar.signOut') }}
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>
