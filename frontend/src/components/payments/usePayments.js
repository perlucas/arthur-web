import { ref } from 'vue';

// Generate a static set of mock payments
const allPayments = Array.from({ length: 50 }, (_, i) => ({
  id: i,
  timestamp: new Date(Date.now() - i * 30 * 24 * 60 * 60 * 1000), // Stagger timestamps by month
  description: `Monthly Subscription - Plan X`,
  amount: 49.99,
}));

export function usePayments() {
  const payments = ref([]);
  const totalRecords = ref(allPayments.length);
  const loading = ref(false);

  const fetchPayments = (page, rows) => {
    return new Promise((resolve) => {
      loading.value = true;
      setTimeout(() => {
        const start = page * rows;
        const end = start + rows;
        payments.value = allPayments.slice(start, end);
        loading.value = false;
        resolve();
      }, 300);
    });
  };

  return {
    payments,
    totalRecords,
    loading,
    fetchPayments,
  };
}
