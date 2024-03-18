export class Component {
    #element = null

    constructor(tag, parent, options) {
        this.tag = tag
        this.parent = parent
        this.options = options
    }
}