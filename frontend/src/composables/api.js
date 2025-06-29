import axios from 'axios';
import { readonly, ref } from 'vue';

export const useReadOperation = (args) => {
  const dataRef = ref(null);
  const errorRef = ref(null);
  const loadingRef = ref(false);

  const { url, headers = {} } = args;

  const refresh = () => {
    loadingRef.value = true;

    axios
      .get(url, {
        headers,
      })
      .then((data) => {
        dataRef.value = data.data;
        errorRef.value = null;
      })
      .catch((err) => {
        errorRef.value = err;
        dataRef.value = null;
      })
      .finally(() => {
        loadingRef.value = false;
      });
  };

  refresh();

  return {
    loading: readonly(loadingRef),
    data: readonly(dataRef),
    error: readonly(errorRef),
    refresh,
  };
};

export const useWriteOperation = (args) => {
  const loadingRef = ref(false);

  const { operation } = args;

  const mutate = async (...params) => {
    loadingRef.value = true;

    try {
      const data = await operation(axios, ...params);
      return { data, error: null };
    } catch (error) {
      return { data: null, error };
    } finally {
      loadingRef.value = false;
    }
  };

  return {
    loading: readonly(loadingRef),
    mutate,
  };
};
