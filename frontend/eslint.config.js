import js from '@eslint/js';
import globals from 'globals';
import pluginVue from 'eslint-plugin-vue';

export default [
  js.configs.recommended,
  ...pluginVue.configs['flat/strongly-recommended'],
  {
    ignores: ['dist/', 'node_modules/'],
    plugins: { vue: pluginVue },
    languageOptions: {
      sourceType: 'module',
      globals: globals.browser,
    },
    rules: {
      'prefer-const': 'error',
      'vue/multi-word-component-names': 'off',
      'vue/singleline-html-element-content-newline': 'off',
      'vue/html-self-closing': 'off',
      'vue/max-attributes-per-line': 'off',
      'no-unused-vars': ['error', { varsIgnorePattern: '^_+', argsIgnorePattern: '^_+' }],
    },
  },
];
