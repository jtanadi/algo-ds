// Stack implemented with JS Array, using a constructor function

function Stack() {
  this.container = []
}

Stack.prototype.push = function(item) {
  this.container.push(item)
}

Stack.prototype.pop = function(idx = null) {
  if (idx) {
    const itemToReturn = this.container[idx]
    this.container = this.container.filter((item, _idx) => idx !== _idx)
    return itemToReturn
  }
  return this.container.pop()
}

Stack.prototype.size = function() {
  return this.container.length
}

Stack.prototype.isEmpty = function() {
  return !this.container.length
}

Stack.prototype.serialize = function() {
  return this.container.join("-")
}

const s = new Stack()
s.push("hello")
s.push(4)
console.log(s.size()) // 2
console.log(s.isEmpty()) // false
console.log(s.serialize()) // "hello-4"
console.log(s.pop()) // 4
console.log(s.pop()) // "hello"
console.log(s.isEmpty()) // true

