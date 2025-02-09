import defaultTheme from "tailwindcss/defaultTheme";

module.exports = {
    darkMode: "class",
    content: [
        "./node_modules/preline/preline.js",
        "./templates/**/*.{html,js,py}",
        "!./templates/admin/**/*.{html,js,py}",
        "./common/**/*.{html,js}",
        "./users/**/*.{html,js}",
    ],
    theme: {
        extend: {
            colors: {
                foreground: "hsl(var(--foreground))",
                background: "hsl(var(--background))",
                card: "hsl(var(--card))",
                border: "hsl(var(--border))",
                primary: "hsl(var(--primary))",
                accent: "hsl(var(--accent))",
            },
        },
    },
    darkMode: "class",
    plugins: [
        require("@tailwindcss/typography"),
        require("tailwindcss-intersect"),
        require("tailwindcss-motion"),
        require("@tailwindcss/forms"),
        require("preline/plugin"),
    ],
};
