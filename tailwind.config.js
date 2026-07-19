/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        cyber: {
          bg: '#0B1120',
          panel: '#111827',
          card: '#1E293B',
          border: '#334155',
          accent: '#22D3EE',
          success: '#10B981',
          warning: '#F59E0B',
          danger: '#EF4444',
          critical: '#DC2626',
        },
      },
      fontFamily: {
        mono: ['JetBrains Mono', 'monospace'],
      },
    },
  },
  plugins: [],
};
