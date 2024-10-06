module.exports = {
    chainWebpack: config => {
      config.module
        .rule('js')
        .include.add(/node_modules\/axios/)  // 指定 axios 路径
        .end()
        .use('babel-loader')
        .loader('babel-loader')
        .tap(options => {
          options.presets = ['@babel/preset-env'];
          return options;
        });
    }
  };
  