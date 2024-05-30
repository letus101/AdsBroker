/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './templates/**/*.html',
      './chat/templates/**/*.html',
      './Articles/templates/**/*.js',
      './AdsFavorites/templates/**/*.html',
      './node_modules/flowbite/**/*.js',
      './**/**/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
      require('flowbite/plugin'),
  ],
}

