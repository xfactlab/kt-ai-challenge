const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.(csv|xlsx|xls)$/,
          loader: 'file-loader',
          options: {
            name: `files/[name].[ext]`
          }
        }
      ],
     },
  },
  pages : {
    index : {
      entry:'src/main.js',
      title : "KT믿:음-xfact팀"
    }
  },
  devServer : {
    proxy : {
      '/' : {
        target :  process.env.VUE_APP_SERVER_URL,
        changeOrigin : true,
        secure : false,
      }
    }
  },
  lintOnSave : false,
  transpileDependencies: true,

})
