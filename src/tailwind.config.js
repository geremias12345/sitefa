/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './templates/**/*.html',   // plantillas globales
    './apps/**/*.html',        // plantillas en apps
    './core/**/*.html',        // plantillas del core
    './**/*.js',               // scripts
    './static/src/css/**/*.css' // css fuente
  ],
  theme: {
    extend: {
      colors: {
        primary: '#2563eb',
        secondary: '#facc15',
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui'],
      },
    },
  },
  plugins: [],
};
