class Stack(object):
    def __init__(self):
        self.container = []

    def __len__(self):
        """
        dunder method implementation of size()
        """
        return len(self.container)

    def __str__(self):
        """
        Return stack as string, delimited by "-"
        """
        return "-".join([str(item) for item in self.container])

    def push(self, item):
        self.container.append(item)

    def pop(self, idx = None):
        if idx is None:
            return self.container.pop()
        else:
            item_to_return = self.container[idx]
            self.container = [item for i, item in enumerate(self.container) if i != idx]
            return item_to_return

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return not len(self.container)

if __name__ == "__main__":
    s = Stack()
    print(s.is_empty()) # True
    s.push(4)
    s.push('dog')
    print(s.peek()) # 'dog'
    print(s.pop()) # 'dog'
    s.push('cat')
    s.push(100)
    print(s.pop(1)) # 'cat'
    print(len(s)) # 2
    print(s) # 4-100
