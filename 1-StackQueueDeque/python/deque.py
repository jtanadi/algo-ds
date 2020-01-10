class Deque(object):
    def __init__(self):
        self.container = []

    def __len__(self):
        return len(self.container)

    def __str__(self):
        return "-".join([str(item) for item in self.container])

    def add_front(self, item):
        self.container.insert(0, item)

    def add_rear(self, item):
        self.container.append(item)

    def remove_front(self):
        return self.container.pop(0)

    def remove_rear(self):
        return self.container.pop()

    def is_empty(self):
        return not len(self.container)

if __name__ == "__main__":
    d = Deque()
    print(d.is_empty()) # True
    d.add_rear(4)
    d.add_rear("dog")
    d.add_front("cat")
    d.add_front(True)
    print(len(d)) # 4
    print(d.is_empty()) # False
    print(d.remove_front()) # True
    print(d.remove_rear()) # "dog"
    print(d) # "cat-4"
