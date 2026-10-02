/** @type {import('tailwindcss').Config} */

/* Semantic tokens resolve to CSS custom properties declared in src/app.src.css.
   Light and dark themes simply redefine those properties, so every component
   below inherits both themes without a single `dark:` utility. */
const token = (name) => `rgb(var(--c-${name}) / <alpha-value>)`;

module.exports = {
  darkMode: ['selector', '.mi-dark'],
  content: ['./*.html', './guides/*.html', './downloads/*.html', './assets/js/*.js'],
  safelist: [
    'is-correct', 'is-incorrect', 'is-revealed',
    'tone-good', 'tone-mid', 'tone-bad',
  ],
  theme: {
    extend: {
      colors: {
        /* ---- semantic surface + text tokens (theme aware) ---- */
        canvas: token('canvas'),
        surface: token('surface'),
        raise: token('raise'),
        sunken: token('sunken'),
        line: { DEFAULT: token('line'), strong: token('line-strong') },
        strong: token('strong'),
        body: token('body'),
        soft: token('soft'),
        faint: token('faint'),
        accent: {
          DEFAULT: token('accent'),
          hover: token('accent-hover'),
          fg: token('accent-fg'),
          soft: token('accent-soft'),
          'soft-fg': token('accent-soft-fg'),
          line: token('accent-line'),
          text: token('accent-text'),
        },
        warn: {
          DEFAULT: token('warn'),
          fg: token('warn-fg'),
          soft: token('warn-soft'),
          'soft-fg': token('warn-soft-fg'),
          line: token('warn-line'),
        },
        bad: {
          DEFAULT: token('bad'),
          soft: token('bad-soft'),
          'soft-fg': token('bad-soft-fg'),
          line: token('bad-line'),
        },
        invert: { DEFAULT: token('invert-bg'), fg: token('invert-fg'), soft: token('invert-soft') },

        /* ---- raw earthy scales, still available where a fixed hue is wanted ---- */
        ink: {
          50: '#f7f6f4', 100: '#eeebe6', 200: '#ddd8d0', 300: '#c3bcaf', 400: '#a39a8a',
          500: '#857c6c', 600: '#6b6355', 700: '#564f44', 800: '#3b362e', 900: '#272420', 950: '#171513',
        },
        clay: {
          50: '#fdf4f2', 100: '#fbe6e1', 200: '#f6cdc4', 300: '#eda99a', 400: '#e07c67',
          500: '#cf5740', 600: '#b4432f', 700: '#953627', 800: '#7a3024', 900: '#662c23', 950: '#37130d',
        },
      },
      fontFamily: {
        sans: ['ui-sans-serif', 'system-ui', '-apple-system', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
        display: ['ui-serif', 'Georgia', 'Cambria', 'Times New Roman', 'serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'Consolas', 'monospace'],
      },
      boxShadow: {
        card: '0 1px 2px rgb(var(--c-shadow) / .05), 0 6px 20px -14px rgb(var(--c-shadow) / .3)',
        lift: '0 2px 4px rgb(var(--c-shadow) / .06), 0 16px 36px -22px rgb(var(--c-shadow) / .45)',
        pop: '0 12px 32px -10px rgb(var(--c-shadow) / .35)',
      },
      maxWidth: { prose: '68ch', page: '78rem' },
      ringColor: { DEFAULT: token('accent') },
    },
  },
  plugins: [],
};
