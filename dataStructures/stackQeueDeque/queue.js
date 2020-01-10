// Queue implemented with JS Array, using class

class Queue {
  constructor() {
    this.container = []
  }

  size() {
    return this.container.length
  }

  isEmpty() {
    return !this.container.length
  }

  enqueue(item) {
    // Sequence is reversed: new item is inserted in front
    // and removed from back
    this.container = [item, ...this.container]

    // Could also use
    // this.container.unshift(item)
  }

  dequeue(item) {
    return this.container.pop()
  }

  serialize() {
    return this.container.join("-")
  }
}

const q = new Queue()
console.log(q.size()) // 0
q.enqueue('hello')
q.enqueue('world')
console.log(q.size()) // 2
console.log(q.serialize()) // 'world-hello'
console.log(q.dequeue()) // 'hello'
console.log(q.isEmpty()) // false
