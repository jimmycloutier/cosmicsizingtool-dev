var webpack = require('webpack');
var path = require('path');
var merge = require('webpack-merge');
var TARGET = process.env.npm_lifecycle_event;


var BUILD_DIR = path.resolve(__dirname, 'src/client/public');
var APP_DIR = path.resolve(__dirname, 'src/client/app');

var config = {
  entry: {
      //bundle: APP_DIR + '/appGuide.jsx',
      bundle: APP_DIR + '/index.js',
      //text: APP_DIR + '/draftJS.jsx',
      //squire: APP_DIR + '/squire.jsx',
      //cooccur: APP_DIR + '/cooccur.jsx'
  },
  output: {
    path: BUILD_DIR,
    filename: '[name].js'
  },
  plugins: [
          new webpack.ResolverPlugin([
              new webpack.ResolverPlugin.DirectoryDescriptionFilePlugin("bower.json", ["main"])
          ])
      ],
  module : {
    loaders : [
      {
        test : /\.jsx?/,
        include : APP_DIR,
        loader : 'babel'
      },
      {
        test: /\.css$/,
        loaders: [
          'isomorphic-style-loader',
          "css-loader?sourceMap&modules&localIdentName=[local]",
          'postcss-loader?parser=postcss-scss',
        ],
      },
      { test: /\.less$/, loader: "style!css!less" },
      {
        test: /\.scss$/,
        loaders: [
          'isomorphic-style-loader',
          "css-loader?${DEBUG ? 'sourceMap&' : 'minimize&'}modules&localIdentName=" +
          "${DEBUG ? '[name]_[local]_[hash:base64:3]' : '[hash:base64:4]'}",
          'postcss-loader?parser=postcss-scss',
        ],
      },
      {
        test: /\.json$/,
        loader: 'json-loader',
      }, {
        test: /\.txt$/,
        loader: 'raw-loader',
      }, {
        test: /\.(png|jpg|jpeg|gif|svg|woff|woff2)$/,
        loader: 'url-loader?limit=10000',
      }
      ,
      {
        test: /\.(eot|ttf)$/,
        loader: 'file-loader',
      }
    ]
  },

  //,watch: true
};

// Default configuration. We will return this if
// Webpack is called outside of npm.
if(TARGET === 'start' || !TARGET) {

module.exports = merge(config, {

    devtool: 'eval-source-map',
    devServer: {
     historyApiFallback: true
   }

  });

}

if(TARGET === 'dev' || TARGET === 'build' ) {
  module.exports = merge(config,{});
}

if(TARGET === 'prod' ) {
  module.exports = merge(config, {
    plugins: [
      new webpack.optimize.UglifyJsPlugin({
        compress: {
          warnings: false
        }
      })
      ,new webpack.DefinePlugin({
        'process.env.NODE_ENV': '"production"'})
    ]
  });
}
if(TARGET === 'min' ) {
  module.exports = merge(config, {
    plugins: [
      new webpack.optimize.UglifyJsPlugin({
        compress: {
          warnings: false
        }
      })
      ,new webpack.DefinePlugin({
        'process.env.NODE_ENV': '"production"'})
    ]
  });
}

//module.exports = config;
