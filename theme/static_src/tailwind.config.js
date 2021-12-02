/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    /**
     * Stylesheet generation mode.
     *
     * Set mode to "jit" if you want to generate your styles on-demand as you author your templates;
     * Set mode to "aot" if you want to generate the stylesheet in advance and purge later (aka legacy mode).
     */
    mode: "jit",

    purge: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */
        // '../../../templates/**/*.html',
    ],
    darkMode: true, // or 'media' or 'class'
    theme: {
        extend: {
            colors: {
                cgray: {
                    100: "#a9a9a9",
                    200: "9#79799",
                    300: '#878789',
                    400: "#767678",
                    DEFAULT: '#656567',
                    500: "#555557",
                    600: "#2c2e32",
                    700: "#212327",
                    800: "#191a1e",
                    900: "#111113"
                }
            },
            typography: {
                DEFAULT: {
                    css: {
                        color: '#ffffff',
                        a: {
                            color: '#3182ce',
                            '&:hover': {
                                color: '#2c5282',
                            },
                        },
                        h1: {
                            color: "#ffffff"
                        },
                        h2: {
                            color: "#ffffff"
                        },
                        h3: {
                            color: "#ffffff"
                        },
                        pre: {
                            color: "#ffffff",
                            backgroundColor: "#212327"
                        },
                        blockquote: {
                            color: "#767678"
                        }
                    },
                },
            },
        },
    },
    variants: {
        extend: {},
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
