import { ref, watch } from 'vue';
import { useI18n } from 'vue-i18n';
import { format, formatDistanceToNow } from 'date-fns';
import { enUS, es } from 'date-fns/locale';

const localeMap = {
  en: enUS,
  es: es,
};

export function useDateFns() {
  const { locale } = useI18n();
  const dateFnsLocale = ref(localeMap[locale.value] || enUS);

  watch(locale, (newLocale) => {
    dateFnsLocale.value = localeMap[newLocale] || enUS;
  });

  const formatDate = (date, formatString = 'PPpp') => {
    return format(new Date(date), formatString, {
      locale: dateFnsLocale.value,
    });
  };

  const formatDistance = (date) => {
    return formatDistanceToNow(new Date(date), {
      addSuffix: true,
      locale: dateFnsLocale.value,
    });
  };

  return {
    formatDate,
    formatDistance,
  };
}
