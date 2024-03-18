class Author {
    constructor(name, posts) {
        this.name = name
        this.posts = posts 
    }

    savePost(post) {
        this.writePost(this.name)
    }
}

module.exports = Author