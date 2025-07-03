export default {
  content: ['./**/*.html'],
  theme: {
    extend: {
      keyframes: {
        fade: {
          '0%, 100%': { opacity: '0' },
          '10%, 90%': { opacity: '1' },
        },
        'slide-left': {
          from: { transform: 'translateX(0)' },
          to: { transform: 'translateX(-100%)' },
        },
      },
      animation: {
        'fade-image-1': 'fade 12s infinite',
        'fade-image-2': 'fade 12s infinite 4s',
        'fade-image-3': 'fade 12s infinite 8s',
        'slide-left-infinite': 'slide-left 15s linear infinite',
      },
    },
  },
  plugins: [],
}
