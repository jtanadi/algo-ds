class BSTNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        <= goes left
        > goes right
        """
        new_node = BSTNode(value)

        if self.root is None:
            self.root = new_node
        else:
            node = self.root
            while True:
                if new_node.value <= node.value:
                    if node.left is None:
                        node.left = new_node
                        new_node.parent = node
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new_node
                        new_node.parent = node
                        break
                    node = node.right
        return new_node

    def find(self, input_node):
        node = self.root

        value = input_node
        if isinstance(input_node, BSTNode):
            value = input_node.value

        while node:
            if value == node.value:
                return node
            elif value < node.value:
                node = node.left
            else:
                node = node.right

        return None

    def find_min(self):
        return self.find_min_subtree(self.root)

    def find_min_subtree(self, subtree_root):
        """
        Find min node of subtree starting at subtree_root
        """
        if subtree_root is None:
            return None
        else:
            node = subtree_root
            while node.left:
                node = node.left
            return node

    def find_max(self):
        return self.find_max_subtree(self.root)

    def find_max_subtree(self, subtree_root):
        """
        Find max node of subtree starting at subtree_root
        """
        if subtree_root is None:
            return None
        else:
            node = subtree_root
            while node.right:
                node = node.right
            return node

    def find_next_larger(self, input_node):
        found = self.find(input_node)
        if found is None:
            return None

        if found.right:
            return self.find_min_subtree(found.right)
        else:
            parent = found.parent
            while parent.value <= found.value:
                if parent == self.root:
                    break
                parent = parent.parent

            if parent.value <= found.value:
               return None

            return parent

    def find_next_larger_val(self, input_node):
        """
        Convenience function to return value of node (or None)
        """
        next_larger = self.find_next_larger(input_node)
        if next_larger is None:
            return next_larger
        else:
            return next_larger.value

    def delete(self, input_node):
        found = self.find(input_node)
        parent = found.parent

        if found.left is None and found.right is None:
            if found.value > parent.value:
                parent.right = None
            else:
                parent.left = None

        elif found.left is None:
            if found.value > parent.value:
                parent.right = found.right
            else:
                parent.left = found.right
            found.right.parent = parent
            found = None

        elif found.right is None:
            if found.value > parent.value:
                parent.right = found.left
            else:
                parent.left = found.left
            found.left.parent = parent
            found = None

        else:
            next_larger = self.find_next_larger(found)
            next_larger_val = next_larger.value
            self.delete(next_larger)
            found.value = next_larger_val

    def __str__(self):
        """
        BFS serialization
        Returns node values separated by "-"

        Given:
            20
          /    \
         10    30
        /  \  /  \
        N  15 N  N

        Return 20-10-30-None-15
        """
        node = self.root
        nodes = [node]
        vals = []

        while nodes:
            node = nodes[0]
            nodes = nodes[1:]

            if node:
                vals.append(node.value)
                if node.left or node.right:
                    nodes.append(node.left)
                    nodes.append(node.right)
            else:
                vals.append(None)

        return "-".join([str(val) for val in vals])


if __name__ == "__main__":
    myBST = BST()
    myBST.insert(20)
    myBST.insert(10)
    myBST.insert(15)
    myBST.insert(30)
    myBST.insert(45)
    myBST.insert(5)

    """
                20
            /        \
           10        30
          /  \      /  \
         5   15   None 45

    """

    print(myBST) # 20-10-30-5-15-None-45

    bstMin = myBST.find_min()
    bstMax = myBST.find_max()
    print(bstMin.value) # 5
    print(bstMax.value) # 45
    print(myBST.find_next_larger_val(bstMin)) # 10
    print(myBST.find_next_larger_val(15)) # 20
    print(myBST.find_next_larger_val(45)) # None

    myBST.insert(4)
    myBST.insert(3)
    myBST.insert(55)
    myBST.insert(50)
    myBST.insert(18)

    """
                20
            /        \
           10        30
          /  \      /  \
         5   15   None  45
        /      \         \
       4       18        55
      /                 /
     3                 50
    """

    print(myBST.find_next_larger_val(3)) # 4
    print(myBST.find_next_larger_val(4)) # 5
    print(myBST.find_next_larger_val(15)) # 18
    print(myBST.find_next_larger_val(45)) # 50
    print(myBST.find_next_larger_val(55)) # None

    myBST.delete(4)
    """
                20
            /        \
           10        30
          /  \      /  \
         5   15   None  45
        / \  / \       / \
       3  N  N 18     N  55
                        /  \
                       50  None
    """
    print(myBST) # 20-10-30-5-15-None-45-3-None-None-18-None-55-50-None

    myBST.delete(3)
    """
                20
            /        \
           10        30
          /  \      /  \
         5   15   None  45
             / \       / \
             N 18     N  55
                        /  \
                       50  None
    """
    print(myBST) # 20-10-30-5-15-None-45-None-18-None-55-50-None

    myBST.delete(15)
    """
                20
            /        \
           10        30
          /  \      /  \
         5   18   None  45
                       / \
                      N  55
                        /  \
                       50  None
    """
    print(myBST) # 20-10-30-5-18-None-45-None-55-50-None

    myBST.delete(55)
    """
                20
            /        \
           10        30
          /  \      /  \
         5   18   None  45
                       / \
                      N  50
    """
    print(myBST) # 20-10-30-5-18-None-45-None-50

    myBST.delete(10)
    """
                20
            /        \
           18        30
          /  \      /  \
         5    N   None  45
                       / \
                      N  50
    """
    print(myBST) # 20-18-30-5-None-None-45-None-50

    myBST.insert(25)
    myBST.insert(35)

    """
                20
            /        \
           18        30
          /  \      /  \
         5    N    25   45
                       / \
                     35  50
    """
    print(myBST) # 20-18-30-5-None-25-45-35-50

    myBST.delete(30)
    """
                20
            /        \
           18        35
          /  \      /  \
         5    N    25   45
                       / \
                    None 50
    """
    print(myBST) # 20-18-35-5-None-25-45-None-50

    myBST.delete(35)
    """
                20
            /        \
           18        45
          /  \      /  \
         5    N    25   50
    """
    print(myBST) # 20-18-45-5-None-25-50

    myBST.delete(5)
    myBST.delete(50)
    myBST.delete(20)
    """
                25
            /        \
           18        45
    """
    print(myBST) # 25-18-45
