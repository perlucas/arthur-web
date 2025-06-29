import { createApp } from 'vue';
import PrimeVue from 'primevue/config';
import Nora from '@primeuix/themes/nora';
import { definePreset } from '@primeuix/themes';
import './style.css';
import App from './App.vue';
import { router } from './router';
import { i18n } from './i18n';
import { Tooltip } from 'primevue';

const app = createApp(App);

const Noir = definePreset(Nora, {
  semantic: {
    primary: {
      50: '{zinc.50}',
      100: '{zinc.100}',
      200: '{zinc.200}',
      300: '{zinc.300}',
      400: '{zinc.400}',
      500: '{zinc.500}',
      600: '{zinc.600}',
      700: '{zinc.700}',
      800: '{zinc.800}',
      900: '{zinc.900}',
      950: '{zinc.950}',
    },
    colorScheme: {
      light: {
        primary: {
          color: '{zinc.950}',
          inverseColor: '#ffffff',
          hoverColor: '{zinc.900}',
          activeColor: '{zinc.800}',
        },
        highlight: {
          background: '{zinc.950}',
          focusBackground: '{zinc.700}',
          color: '#ffffff',
          focusColor: '#ffffff',
        },
      },
      dark: {
        primary: {
          color: '{zinc.50}',
          inverseColor: '{zinc.950}',
          hoverColor: '{zinc.100}',
          activeColor: '{zinc.200}',
        },
        highlight: {
          background: 'rgba(250, 250, 250, .16)',
          focusBackground: 'rgba(250, 250, 250, .24)',
          color: 'rgba(255,255,255,.87)',
          focusColor: 'rgba(255,255,255,.87)',
        },
      },
    },
  },
  components: {
    dataview: {
      colorScheme: {
        dark: {
          content: {
            background: 'bg-transparent',
          },
        },
      },
    },
    chip: {
      colorScheme: {
        dark: {
          root: {
            background: '{surface.200}',
            color: '{primary.800}',
          },
        },
      },
    },
    dialog: {
      colorScheme: {
        dark: {
          root: {
            background: '{gray.900}',
          },
        },
      },
    },
    inputtext: {
      colorScheme: {
        dark: {
          root: {
            disabledBackground: '{gray.800}',
          },
        },
      },
    },
    datatable: {
      colorScheme: {
        dark: {
          header: {
            cell: {
              background: '{gray.800}',
            },
          },
          row: {
            background: '{gray.800}',
            hoverBackground: '{gray.700}',
          },
          paginatorBottom: {
            borderWidth: 0,
          },
        },
      },
    },
    paginator: {
      colorScheme: {
        dark: {
          root: {
            background: '{gray.800}',
          },
          navButton: {
            selectedBackground: '{gray.700}',
            hoverBackground: '{gray.900}',
          },
        },
      },
    },
  },
});

app.directive('tooltip', Tooltip);

app.use(PrimeVue, {
  theme: {
    preset: Noir,
  },
});

app.use(router);

app.use(i18n);

app.mount('#app');
