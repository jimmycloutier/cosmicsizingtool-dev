var webpack = require('webpack');
var path = require('path');
var merge = require('webpack-merge');
//var validate = require('webpack-validator');
var TARGET = process.env.npm_lifecycle_event;

var BUILD_DIR = path.resolve(__dirname, 'src/client/public');
var APP_DIR = path.resolve(__dirname, 'src/client/app');
var STYLE_PATH = path.resolve(__dirname, 'style');
// Répertoire où se situent les fichiers .js d'où sont tirées les données de
// localisation.
var LOCALES_JS_DIR = path.resolve(__dirname, '.');

const ExtractTextPlugin = require('extract-text-webpack-plugin');
const WebpackShellPlugin = require('webpack-shell-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

function minify() {
    return {
        plugins: [
            new webpack.LoaderOptionsPlugin({
                minimize: true
            }),
            new UglifyJsPlugin({
                uglifyOptions: {
                    warnings: false,
                    compress: {
                        warnings: false,
                        conditionals: true,
                        unused: true,
                        comparisons: true,
                        sequences: true,
                        dead_code: true,
                        evaluate: true,
                        if_return: true,
                        join_vars: true
                    },
                    output: {
                        comments: false
                    }
                }
            })
            // new webpack.optimize.DedupePlugin(),
            //new webpack.optimize.OccurenceOrderPlugin(true),
            //new webpack.optimize.LimitChunkCountPlugin({maxChunks: 15}),
            //new webpack.optimize.MinChunkSizePlugin({minChunkSize: 10000})
        ]
    };
}


function productionSourceMap() {
    return {
        devtool: 'cheap-module-source-map'
    };
}

function cleanup(path) {
    const CleanWebpackPlugin = require('clean-webpack-plugin');
    const PurifyCSSPlugin = require('purifycss-webpack-plugin');

    return {
        plugins: [
            new CleanWebpackPlugin([path], {
                root: process.cwd()
            }),
            new PurifyCSSPlugin({
                basePath: process.cwd(),
                paths: [path]
            })
        ]
    };
}

function donneLoaderJS(environnement) {
    return ["babel-loader"];
}


function common(environnement) {
    var common = {
        entry: {
            bundle: APP_DIR + '/index.js'
        },
        output: {
            path: BUILD_DIR,
            filename: '[name].js',
            publicPath: '/',
            chunkFilename: '[name].[id].js'
        },
        plugins: [
            new ExtractTextPlugin('[name].css'),
            new webpack.DefinePlugin({'process.env': {NODE_ENV: JSON.stringify(environnement)}})
        ],
        resolve: {
            modules: ["bower_components", "node_modules"]
        },
        module: {
            rules: [
                {
                    test: /\.jsx?/,
                    include: APP_DIR,
                    use: donneLoaderJS(environnement),
                    exclude: [/node_modules/]
                }, {
                    test: /\.css$/,
                    include: STYLE_PATH,
                    use: ExtractTextPlugin.extract({
                        fallback: "style-loader",
                        use: "css-loader"
                    }),
                    exclude: [/node_modules/]
                },
                {
                    test: /\.less$/,
                    use: ExtractTextPlugin.extract({
                        fallback: "style-loader",
                        use: ["css-loader", "less-loader"]
                    }),
                    exclude: [/node_modules/]
                }, {
                    test: /\.json$/,
                    use: ['json-loader']
                }, {
                    test: /\.txt$/,
                    use: ['raw-loader']
                }, {
                    test: /\.(png|jpg|jpeg|gif|svg|woff|woff2)$/,
                    use: [{loader: "url-loader", options: {limit: 10000}}]
                }, {
                    test: /\.(eot|ttf)$/,
                    use: ['file-loader']
                }]
        },
        node: {
            fs: 'empty'
        }
    };
    return common;
}


module.exports = env => {
    var environnement = env.NODE_ENV;
    var serveur = env.SERVEUR;
    process.env.BABEL_ENV = environnement;
    var config;
    var configServeur = {};
    if (serveur === true) {
        if (environnement === "production") {
            configServeur = {devServer: {historyApiFallback: true}};
        } else {
            configServeur = {
                devServer: {historyApiFallback: true},
                devtool: 'eval-source-map',
                plugins: [
                    new UglifyJsPlugin({sourceMap: true})
                ]
            };
        }
    }
    if (environnement === "production") {
        config = merge(
            common(environnement),
            minify(),
            productionSourceMap(),
            cleanup(BUILD_DIR),
            configServeur
        );
    } else {
        config = merge(common(environnement), configServeur);
    }
    return config;
};
