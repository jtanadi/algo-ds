class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class UnorderedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head is None:
            return None

        return_string = ""

        current = self.head
        while current is not None:
            if current.next is None:
                return_string += str(current.value)
            else:
                return_string += str(current.value) + "-"
            current = current.next

        return return_string

    def __len__(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    def add(self, item):
        """
        Add new node to front
        """
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            node = Node(item)
            node.next = self.head
            self.head = node

    def remove(self, item):
        """
        Remove item if found in linked list
        If not found, return False
        """
        # In case item is at the head of our list
        if self.head.value == item:
            self.head = self.head.next
            return True

        previous = None
        current = self.head
        while current is not None:
            if current.value == item:
                previous.next = current.next
                return True

            previous = current
            current = current.next

        return False

    def search(self, item):
        """
        Return True if item is found, False if not
        """
        current = self.head

        while current is not None:
            if current.value == item:
                return True
            current = current.next

        return False

    def is_empty(self):
        return self.head is None

    def append(item):
        """
        Add node to back
        """
        if self.tail is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            node = Node(item)
            self.tail.next = node
            self.tail = node

    def index(item):
        """
        Return first index of item
        or -1 if item isn't found
        """
        idx = 0
        current = self.head

        while current is not None:
            if current.value == item:
                return idx

            idx += 1
            current = current.next

        return -1

    def insert(self, pos, item):
        """
        Insert at pos, index starting at 0
        """
        if pos > len(self):
            return False
        elif pos == len(self):
            # If pos is 1 greater than last index,
            # assume user wants to append
            return self.append(item)
        elif pos == 0:
            # Just use regular add
            return self.add(item)

        idx = 0
        current = self.head
        previous = None

        while idx < pos and current is not None:
            idx += 1
            previous = current
            current = current.next

        if idx == pos:
            node = Node(item)
            previous.next = node
            node.next = current

    def pop(self, pos = None):
        """
        Unfortunately, since our nodes aren't doubly-linked,
        we still have to traverse to remove last node, even if we have
        reference to tail (we can't do `tail = tail.previous`)
        """
        if self.head is None or (pos is not None and pos >= len(self)):
            # Empty list or pos beyond list length
            return False
        elif self.head.next is None:
            # List only has 1 node
            value = self.head.value
            self.head = None
            return value
        elif pos is not None and pos == 0:
            # Removing first item
            value = self.head.value
            self.head = self.head.next
            return value
        elif pos is None or pos == len(self) - 1:
            # Regular pop(). If pos is last index,
            # assume user wants regular pop()
            previous = None
            current = self.head

            while current.next is not None:
                previous = current
                current = current.next

            previous.next = None
            return current.value
        else:
            # Pop with index
            idx = 0
            previous = None
            current = self.head

            while idx < pos and current.next is not None:
                idx += 1
                previous = current
                current = current.next

            if idx == pos:
                previous.next = current.next
                return current.value


if __name__ == "__main__":
    ll = UnorderedList()
    ll.add(3)
    ll.add(6)
    ll.add(1)
    print(ll)
    ll.pop()
    ll.add(5)
    print(ll)
    ll.pop(1)
    print(ll)
    ll.add(100)
    print(ll)
    ll.pop(0)
    print(ll)
    ll.add(200)
    print(ll)
    print(ll.pop(1))
    print(ll)
