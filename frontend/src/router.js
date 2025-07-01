import { createRouter, createWebHistory } from 'vue-router';
import HomeView from './components/home/HomeView.vue';
import DashboardView from './components/dashboard/DashboardView.vue';
import ResultsView from './components/search-results/ResultsView.vue';
import Error404 from './components/error-page/Error404.vue';
import NotificationsView from './components/notifications/NotificationsView.vue';
import PaymentsView from './components/payments/PaymentsView.vue';

const routes = [
  { path: '/', component: HomeView },
  { path: '/dashboard', component: DashboardView },
  { path: '/notifications', component: NotificationsView },
  { path: '/payments', component: PaymentsView },
  { path: '/show-results/:searchId', component: ResultsView },
  { path: '/error-404', component: Error404 },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
