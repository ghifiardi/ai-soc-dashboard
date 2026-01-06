/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          dark: '#0A0E27',
          blue: '#0066FF',
          cyan: '#00D4FF',
        },
        accent: {
          green: '#00C896',
          amber: '#FFB800',
          red: '#FF3B30',
          purple: '#9F7AEA',
        },
        glass: {
          bg: 'rgba(255, 255, 255, 0.03)',
          border: 'rgba(255, 255, 255, 0.1)',
        },
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'glow': 'glow 3s ease-in-out infinite alternate',
      },
      keyframes: {
        glow: {
          '0%': { filter: 'drop-shadow(0 0 20px rgba(0, 212, 255, 0.4))' },
          '100%': { filter: 'drop-shadow(0 0 30px rgba(159, 122, 234, 0.6))' },
        },
      },
      backdropBlur: {
        xs: '2px',
      },
    },
  },
  plugins: [],
};
