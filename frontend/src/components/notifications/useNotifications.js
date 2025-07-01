import { ref } from 'vue';

// Generate a static set of mock notifications
const allNotifications = Array.from({ length: 100 }, (_, i) => ({
  id: i,
  message: `New results for <strong>Search #${i % 5}</strong> have been found.`,
  timestamp: new Date(Date.now() - i * 3 * 60 * 60 * 1000), // Stagger timestamps
  isRead: i > 10, // Mark the first 10 as unread
}));

export function useNotifications() {
  const notifications = ref([]);
  const totalRecords = ref(allNotifications.length);
  const loading = ref(false);

  const fetchNotifications = (page, rows) => {
    return new Promise((resolve) => {
      loading.value = true;
      setTimeout(() => {
        const start = page * rows;
        const end = start + rows;
        notifications.value = allNotifications.slice(start, end);
        loading.value = false;
        resolve();
      }, 300);
    });
  };

  const toggleRead = (id, isRead) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        const notification = allNotifications.find((n) => n.id === id);
        if (notification) {
          notification.isRead = isRead;
        }
        resolve();
      }, 200);
    });
  };

  const deleteNotification = (id) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        const index = allNotifications.findIndex((n) => n.id === id);
        if (index !== -1) {
          allNotifications.splice(index, 1);
          totalRecords.value = allNotifications.length;
        }
        resolve();
      }, 200);
    });
  };

  return {
    notifications,
    totalRecords,
    loading,
    fetchNotifications,
    toggleRead,
    deleteNotification,
  };
}
