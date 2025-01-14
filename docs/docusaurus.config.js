/* eslint-disable global-require,import/no-extraneous-dependencies */

// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion
// eslint-disable-next-line import/no-extraneous-dependencies
const { ProvidePlugin } = require("webpack");
require("dotenv").config();

const prism = require("prism-react-renderer");

const baseLightCodeBlockTheme = prism.themes.vsLight;
const baseDarkCodeBlockTheme = prism.themes.vsDark;

const baseUrl = "/";

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "🦜️🔗 AIAgentsForce",
  tagline: "AIAgentsForce Python Docs",
  favicon: "img/brand/favicon.png",
  // Set the production url of your site here
  url: "https://docs.aiagentsforce.com",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: baseUrl,
  trailingSlash: true,
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "throw",
  onBrokenAnchors: "throw",

  themes: ["@docusaurus/theme-mermaid"],
  markdown: {
    mermaid: true,
  },

  plugins: [
    () => ({
      name: "custom-webpack-config",
      configureWebpack: () => ({
        plugins: [
          new ProvidePlugin({
            process: require.resolve("process/browser"),
          }),
        ],
        resolve: {
          fallback: {
            path: false,
            url: false,
          },
        },
        module: {
          rules: [
            {
              test: /\.m?js/,
              resolve: {
                fullySpecified: false,
              },
            },
            {
              test: /\.py$/,
              loader: "raw-loader",
              resolve: {
                fullySpecified: false,
              },
            },
            {
              test: /\.ya?ml$/,
              use: 'yaml-loader'
            },
            {
              test: /\.ipynb$/,
              loader: "raw-loader",
              resolve: {
                fullySpecified: false,
              },
            },
          ],
        },
      }),
    }),
  ],

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          editUrl: "https://github.com/AI-Agents-Force-SDK/aiagentsforce/edit/main/docs/",
          sidebarPath: require.resolve("./sidebars.js"),
          remarkPlugins: [
            [require("@docusaurus/remark-plugin-npm2yarn"), { sync: true }],
          ],
          async sidebarItemsGenerator({
            defaultSidebarItemsGenerator,
            ...args
          }) {
            const sidebarItems = await defaultSidebarItemsGenerator(args);
            sidebarItems.forEach((subItem) => {
              // This allows breaking long sidebar labels into multiple lines
              // by inserting a zero-width space after each slash.
              if (
                "label" in subItem &&
                subItem.label &&
                subItem.label.includes("/")
              ) {
                // eslint-disable-next-line no-param-reassign
                subItem.label = subItem.label.replace(/\//g, "/\u200B");
              }
              if (args.item.className) {
                subItem.className = args.item.className;
              }
            });
            return sidebarItems;
          },
        },
        pages: {
          remarkPlugins: [require("@docusaurus/remark-plugin-npm2yarn")],
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      docs: {
        sidebar: {
          hideable: true,
          autoCollapseCategories: true,
        },
      },
      colorMode: {
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
      prism: {
        theme: {
          ...baseLightCodeBlockTheme,
          plain: {
            ...baseLightCodeBlockTheme.plain,
            backgroundColor: "#F5F5F5",
          },
        },
        darkTheme: {
          ...baseDarkCodeBlockTheme,
          plain: {
            ...baseDarkCodeBlockTheme.plain,
            backgroundColor: "#222222",
          },
        },
      },
      image: "img/brand/theme-image.png",
      navbar: {
        logo: {src: "img/brand/wordmark.png", srcDark: "img/brand/wordmark-dark.png"},
        items: [
          {
            type: "docSidebar",
            position: "left",
            sidebarId: "integrations",
            label: "Integrations",
          },
          {
            label: "API Reference",
            to: "https://docs.aiagentsforce.com/api_reference/",
          },
          {
            type: "dropdown",
            label: "More",
            position: "left",
            items: [
              {
                type: "doc",
                docId: "contributing/index",
                label: "Contributing",
              },
              {
                type: "doc",
                docId: "people",
                label: "People",
              },
              {
                type: "doc",
                docId: "troubleshooting/errors/index",
                label: "Error reference",
              },
              {
                type: 'html',
                value: '<hr class="dropdown-separator" style="margin-top: 0.5rem; margin-bottom: 0.5rem">',
              },
            ]
          },
          {
            type: "dropdown",
            label: "v0.3",
            position: "right",
            items: [
              {
                label: "v0.3",
                href: "/docs/introduction"
              },
            ]
          },
          {
            to: "https://chat.langchain.com",
            label: "💬",
            position: "right",
          },
          // Please keep GitHub link to the right for consistency.
          {
            href: "https://github.com/AI-Agents-Force-SDK/aiagentsforce",
            position: "right",
            className: "header-github-link",
            "aria-label": "GitHub repository",
          },
        ],
      },
      footer: {
        style: "light",
        links: [
          {
            title: "Community",
            items: [
              {
                label: "Twitter",
                href: "https://x.com/aiagentsforce_",
              },
            ],
          },
          {
            title: "GitHub",
            items: [
              {
                label: "Organization",
                href: "https://github.com/AI-Agents-Force-SDK",
              },
              {
                label: "Python",
                href: "https://github.com/AI-Agents-Force-SDK/aiagentsforce",
              },
            ],
          },
          {
            title: "More",
            items: [
              {
                label: "Homepage",
                href: "https://aiagentsforce.com/",
              },
              {
                label: "AI Agents Directory",
                href: "https://aiagentsdirectory.com/",
              },
            ],
          },
        ],
        //copyright: `Copyright © ${new Date().getFullYear()} AiAgentsForce, Inc.`,
      },
      algolia: {
        // The application ID provided by Algolia
        appId: "VAU016LAWS",

        // Public API key: it is safe to commit it
        // this is linked to erick@langchain.dev currently
        apiKey: "6c01842d6a88772ed2236b9c85806441",

        indexName: "python-aiagentsforce-latest",

        contextualSearch: false,
      },
    }),

  scripts: [
    baseUrl + "js/google_analytics.js",
    {
      src: "https://www.googletagmanager.com/gtag/js?id=G-9B66JQQH2F",
      async: true,
    },
  ],

  customFields: {
    supabasePublicKey: process.env.NEXT_PUBLIC_SUPABASE_PUBLIC_KEY,
    supabaseUrl: process.env.NEXT_PUBLIC_SUPABASE_URL,
  },
};

module.exports = config;
