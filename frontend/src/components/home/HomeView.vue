<script setup>
  import { RouterLink } from 'vue-router';
</script>

<template>
  <div class="m-5">
    <h1 class="text-4xl mb-[1rem]">{{ $t('home.title') }}</h1>
    <router-link to="/dashboard">{{ $t('dashboard.title') }}</router-link>
  </div>
</template>
