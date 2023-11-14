module.exports = {
    entry: {
        index:  './src/index.js',
    },
    mode: 'development',
    module: {
        rules: [{
            // Propriedades:
            test:  /\.css$/, // Quais arquivos vai executar/aplicar o loader.
            use: ['style-loader', 'css-loader'] // dizer qual loader será utilizado
        }]
    }
}