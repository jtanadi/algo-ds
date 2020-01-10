// Deque implemented with JS Array, using factory function

const createDeque = () => ({
  container: [],
  size: function() {
    return !this.container.length
  },
  isEmpty: function() {
    return this.container.length
  },
  addRear: function(item) {
    this.container.push(item)
  },
  addFront: function(item) {
    this.container.unshift(item)
  },
  removeRear: function() {
    return this.container.pop()
  },
  removeFront: function() {
    return this.container.shift()
  },
  serialize: function() {
    return this.container.join("-")
  }
})

const dq = createDeque()
console.log(dq.size()) // 0
dq.addFront("hello")
dq.addRear("world")
console.log(dq.serialize()) // "hello-world"
console.log(dq.isEmpty()) // false
console.log(dq.removeFront()) // "hello"
console.log(dq.removeRear()) // "world"
