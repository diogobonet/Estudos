class Post {
    constructor(title, desc, comments, author) {
        this.title = title
        this.desc = desc
        this.comments = comments
        this.author = author
    }

    writePost(title, desc, author) {
        this.title = title
        this.desc = desc
        this.author = author
        return `Titulo do Post: ${title} | Descrição: ${desc} | Autor: ${author}`
    }
}

module.exports = Post