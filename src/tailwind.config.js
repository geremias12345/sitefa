/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './templates/**/*.html',
    './apps/**/*.html',
    './core/**/*.html',
    './**/*.js',
    './static/src/css/**/*.css'
  ],
  theme: {
    extend: {
      colors: {
        bg: "var(--bg)",
        text: "var(--text)",
        nav: "var(--nav)",
        navtext: "var(--nav-text)",
        panel: "var(--panel)",
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