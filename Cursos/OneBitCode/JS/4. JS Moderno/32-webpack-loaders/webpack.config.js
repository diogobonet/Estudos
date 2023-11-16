const MiniCssExtractPlugin = require('mini-css-extract-plugin')

module.exports = {
    entry: {
        index:  './src/index.js',
    },
    mode: 'development',
    module: {
        rules: [{
            // Propriedades:
            test:  /\.css$/, // Quais arquivos vai executar/aplicar o loader.
            use: [MiniCssExtractPlugin.loader, 'css-loader'] // dizer qual loader será utilizado
        }]
    },
    plugins: [
        new MiniCssExtractPlugin()
    ]
        
}