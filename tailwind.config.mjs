/** @type {import('tailwindcss').Config} */

// One accent colour for the whole site: a deep ink-teal.
// The old design used Tailwind's indigo everywhere (including inside articles),
// so we remap the indigo scale to this accent instead of editing every class.
const accent = {
	50: '#eef6f6',
	100: '#d6eaea',
	200: '#aed4d5',
	300: '#7fb8ba',
	400: '#4f9a9d',
	500: '#2f7f83',
	600: '#21676b',
	700: '#1b5357',
	800: '#184447',
	900: '#16393c',
	950: '#0a2224',
};

export default {
	darkMode: 'class',
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			colors: {
				indigo: accent,
				accent,
				paper: { DEFAULT: '#fbfaf7', dark: '#101314' },
				ink: { DEFAULT: '#16181a', soft: '#4a4f55', mute: '#7a7f86' },
			},
			fontFamily: {
				sans: ['Inter', 'Noto Sans SC', 'system-ui', 'sans-serif'],
				serif: ['Newsreader', 'Noto Serif SC', 'Georgia', 'serif'],
			},
		},
	},
	plugins: [
		require('@tailwindcss/typography'),
	],
}
