function Node(value) {
  this.value = value
  this.next = null
}

class UnorderedList {
  constructor() {
    this.head = null
  }

  serialize() {
    if (!this.head) return null

    const nodes = []
    let current = this.head

    while (current) {
      nodes.push(current.value)
      current = current.next
    }

    return nodes.join("-")
  }

  length() {
    let count = 0
    let current = this.head

    while (current) {
      count += 1
      current = current.next
    }

    return count
  }

  add(item) {
    if (!this.head) {
      this.head = new Node(item)
    } else {
      const newNode = new Node(item)
      newNode.next = this.head
      this.head = newNode
    }
  }

  remove(item) {
    if (this.head.value === item) {
      this.head = this.head.next
      return
    }

    let prev = null
    let current = this.head

    while (current) {
      if (current.value === item) {
        prev.next = current.next
        return
      }

      prev = current
      current = current.next
    }
  }

  search(item) {
    let current = this.head

    while (current) {
      if (current.value === item) return true
      current = current.next
    }

    return false
  }

  isEmpty() {
    return !this.head
  }

  append(item) {
    let current = this.head

    while (current.next) {
      current = current.next
    }

    current.next = new Node(item)
  }

  index(item) {
    let idx = 0
    let current = this.head

    while (current) {
      if (current.value === item) return idx
      idx++
      current = current.next
    }

    return -1
  }

  insert(pos, item) {
    // Some basic catches
    if (pos > this.length()) {
      return
    } else if (pos === this.length()) {
      this.append(item)
    } else if (pos === 0) {
      return this.add(item)
    }

    let idx = 0
    let prev = null
    let current = this.head

    while (idx < pos && current) {
      idx ++
      prev = current
      current = current.next
    }

    if (idx === pos) {
      const node = new Node(item)
      prev.next = node
      node.next = current
    }
  }

  pop(pos) {
    if (!this.head || (pos && pos >= this.length())) {
      // Invalid pop()
      return false
    } else if (!this.head.next) {
      // Only 1 item in list
      const value = this.head.value
      this.head = null
      return value
    } else if (pos === 0) {
      // pop() first item
      const value = this.head.value
      this.head = this.head.next
      return value
    } else if (!pos || pos === this.length() - 1) {
      // pop() last item
      let prev = null
      let current = this.head

      while (current.next) {
        prev = current
        current = current.next
      }

      prev.next = null
      return current.value
    } else {
      // pop() any other index
      let idx = 0
      let prev = null
      let current = this.head

      while (idx < pos && current) {
        idx++
        prev = current
        current = current.next
      }

      if (idx === pos) {
        prev.next = current.next
        return current.value
      }
    }
  }
}

const ul = new UnorderedList()
ul.add(5)
ul.add(1)
ul.append(10)
console.log(ul.serialize())
console.log(ul.index(5))
console.log(ul.pop(1))
console.log(ul.serialize())
ul.insert(1, 100)
console.log(ul.serialize())
console.log(ul.pop())
console.log(ul.serialize())
