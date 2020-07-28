module.exports = {
  themeConfig: {
      // logo
    logo: 'https://www.parksi.top/favicon.ico',
      // 导航栏链接
      nav: [
          {text: 'Home', link: '/' },
          {text: 'Guide', link: '/guide/' },
          {text: 'Get help', link: 'https://shang.qq.com/wpa/qunwpa?idkey=495c8725f2c840f89e9e16c775ced3d15f63b792cb50e04bee0638092be56297', target:'_blank'},
          {text: 'Blog', link: 'https://www.parksi.top', target:'_blank'},
          {text: 'Github', link: 'https://github.com/lparksi/bot', target:'_blank'},
    ],
      // 显示所有页面的标题链接
      displayAllHeaders: false,

      // 侧边栏
      sidebar: 'auto',
  },
    // 标题
    title: 'Bot',
    // 描述
    description: '一个清晰、安全、开放的Nonebot插件库',
    // 输出目录
    dest: 'C:\\Users\\PARKSI\\PycharmProjects\\bot\\docs'
}