const plugin = require("@tailwindcss/forms");

module.exports = {
    darkMode: "class",
    content: [
        "./node_modules/preline/preline.js",
        "./templates/**/*.{html,js,py}",
        "!./templates/admin/**/*.{html,js,py}",
        "./common/**/*.{html,js}",
        "./users/**/*.{html,js}",
    ],
    plugins: [require("@tailwindcss/forms"), require("preline/plugin")],
};
