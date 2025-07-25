// docusaurus-site/docusaurus.config.js
module.exports = {
  title: 'Proactive Docs',
  url: 'https://patlittle.github.io',
  baseUrl: '/proactive-docs/docusaurus/',
  favicon: 'img/favicon.ico',
  organizationName: 'PatLittle',
  projectName: 'proactive-docs',
  themeConfig: {
    navbar: {
      title: 'Proactive Docs',
      items: [
        {to: 'docs/', label: 'Docs', position: 'left'},
      ],
    },
    footer: {
      style: 'dark',
      links: [],
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
