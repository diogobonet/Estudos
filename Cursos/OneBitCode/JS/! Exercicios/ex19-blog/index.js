const Author = require("./Author");
const Post = require("./Post");


let post1 = new Post("O uso da inteligencia artificial", "Eu uso IA a muito tempo!", comment1, author1);
let comment1 = new Comment("Que interessante!")

let author1 = new Author("diogobonet", post1);

console.log(post1)