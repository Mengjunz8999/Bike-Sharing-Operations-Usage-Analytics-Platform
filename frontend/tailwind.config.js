/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        display: ['"Bebas Neue"', "sans-serif"],
        body: ['"DM Sans"', "sans-serif"],
        mono: ['"JetBrains Mono"', "monospace"],
      },
      colors: {
        ink: "#0a0a0f",
        paper: "#f5f2eb",
        lime: "#c8ff00",
        rust: "#e85d26",
        slate: "#2a2a35",
        mist: "#b8b8c8",
      },
    },
  },
  plugins: [],
};
