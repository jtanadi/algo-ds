class Queue(object):
    def __init__(self):
        self.container = []

    def __len__(self):
        """
        dunder implementation of size()
        """
        return len(self.container)

    def enqueue(self, item):
        """
        Insert to front
        """
        self.container.insert(0, item)

    def dequeue(self):
        return self.container.pop()

    def is_empty(self):
        return not len(self.container)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue("Hello")
    q.enqueue("World")
    print(q.dequeue()) # 5
    print(q.dequeue()) # "Hello"
    print(q.dequeue()) # "World"
    print(q.is_empty()) # True

