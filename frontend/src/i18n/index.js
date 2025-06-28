import { createI18n } from 'vue-i18n';
import MessagesEN from './messages.en.json';
import MessagesES from './messages.es.json';

export const i18n = createI18n({
  legacy: false,
  locale: 'es',
  fallbackLocale: 'en',
  messages: {
    en: MessagesEN,
    es: MessagesES,
  },
});
