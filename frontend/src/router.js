import { createMemoryHistory, createRouter } from 'vue-router';
import HomeView from './components/home/HomeView.vue';
import DashboardView from './components/dashboard/DashboardView.vue';

const routes = [
  { path: '/', component: HomeView },
  { path: '/dashboard', component: DashboardView },
];

export const router = createRouter({
  history: createMemoryHistory(),
  routes,
});
