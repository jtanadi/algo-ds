class BSTNode(object):
    """
    `value` is the payload
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BST(object):
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        """
        Overload __setitem__ so we can use
        the list/dict syntax: bst[2] = "hello"
        """
        self.insert(key, value)

    def __getitem__(self, key):
        """
        Overload __getitem__ so we can use
        the list/dict syntax: print(bst[2]) # "hello"
        """
        return self.find(key).value

    def insert(self, key, value = None):
        new_node = BSTNode(key, value)

        if self.root is None:
            self.root = new_node
        else:
            node = self.root
            while True:
                if new_node.key < node.key:
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
        """
        Returns the actual node or
        None when nothing is found
        """
        node = self.root

        # So we can accept a key or a node
        key = input_node
        if isinstance(input_node, BSTNode):
            key = input_node.key

        while node:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right

        return None

    def find_min(self):
        """
        Find min of entire tree
        Returns the actual node
        """
        return self.find_min_subtree(self.root)

    def find_min_subtree(self, subtree_root):
        """
        Find min node of subtree starting at subtree_root
        Returns the actual node
        """
        if subtree_root is None:
            return None
        else:
            node = subtree_root
            while node.left:
                node = node.left
            return node

    def find_max(self):
        """
        Find max of entire tree
        Returns the actual node
        """
        return self.find_max_subtree(self.root)

    def find_max_subtree(self, subtree_root):
        """
        Find max node of subtree starting at subtree_root
        Returns the actual node
        """
        if subtree_root is None:
            return None
        else:
            node = subtree_root
            while node.right:
                node = node.right
            return node

    def find_next_larger(self, input_node):
        """
        Find node with next larger key than input_node
        """
        # Make sure input_node exists first
        found = self.find(input_node)
        if found is None:
            return None

        # Case 1: Next larger is smallest key
        # in the right subtree of current node
        if found.right:
            return self.find_min_subtree(found.right)

        # Case 2: Current node has no right subtree
        # so we go up to parent and look from there
        else:
            parent = found.parent

            # Traverse up until we find the first
            # ancestor whose key is larger than current_node
            while parent.key < found.key:
                if parent == self.root:
                    break
                parent = parent.parent

            # Check, in case we're at the root
            if parent.key < found.key:
               return None

            return parent

    def find_next_larger_val(self, input_node):
        """
        Convenience function to return value of node (or None)
        """
        next_larger = self.find_next_larger(input_node)
        if next_larger is None:
            return None
        else:
            return next_larger.value

    def find_next_smaller(self, input_node):
        """
        Find node with next smaller key than input_node
        """
        # Make sure input_node exists first
        found = self.find(input_node)
        if found is None:
            return None

        # Case 1: Next smaller is the largest key
        # in the left subtree of current node
        if found.left:
            return self.find_max_subtree(found.left)

        # Case 2: Current node has no left subtree,
        # so we go up to parent and look from there
        else:
            parent = found.parent

            # Traverse up until we find the first
            # ancestor whose key is smaller than current node
            while parent.key > found.key:
                if parent == self.root:
                    break
                parent = parent.parent

            # Check, in case we're at the root
            if parent.key > found.key:
                return None

            return parent

    def delete(self, input_node):
        # Simple check to make sure
        # input_node exists in this tree
        found = self.find(input_node)
        parent = found.parent

        # Case 1: node is a leaf (easiest)
        if found.left is None and found.right is None:
            # Better way to check which child found is
            # than doing found.key > parent.key because
            # potentialy cheaper to check memory addresses
            # than keys (ie. if key is some weird object)
            if parent.right == found:
                parent.right = None
            else:
                parent.left = None

        # Case 2A: node has one child (right child)
        # Set current node's parent to current node's child
        elif found.left is None:
            # Same check as above
            if parent.right == found:
                parent.right = found.right
            else:
                parent.left = found.right

            # Make sure to set child's parent reference
            # to its new parent (current's parent)
            found.right.parent = parent

            # Not entirely necessary in py because
            # a dereferenced node will be garbage collected
            # but this is more explicit
            found = None

        # Case 2B: node has one child (left child)
        # Set current node's parent to current node's child
        elif found.right is None:
            # Same steps as above, but mirrored
            if parent.left == found:
                parent.left = found.left
            else:
                parent.right = found.left
            found.left.parent = parent
            found = None

        # Case 3: node has both children
        # So we find next larger (or next smaller) node,
        # which is guaranteed to be a leaf somewhere below current node,
        # we store its (key, value), delete the node recursively
        # (because easiest to delete leaf node)
        # and set the current node's (key, value) to the stored (key, value)
        #      8
        #    /   \
        #   6     10
        #  / \    / \
        # 4   7  9  11

        # use next smaller
        #      7
        #    /   \
        #   6     10
        #  / \    / \
        # 4   N  9  11

        # use next larger
        #      9
        #    /   \
        #   6     10
        #  / \    / \
        # 4   7  N  11
        else:
            next_larger = self.find_next_larger(found)

            next_larger_key = next_larger.key
            next_larger_value = next_larger.value

            self.delete(next_larger)
            found.key = next_larger_key
            found.value = next_larger_value

    def __str__(self):
        """
        BFS serialization
        Returns node (k, v) separated by "-"

        Given:
            20
          /    \
         10    30
        /  \  /  \
        N  15 N  N

        Return (20, v)-(10, v)-(30, v)-None-(15, v)
        """
        node = self.root
        nodes_queue = [node]
        vals = []

        while nodes_queue:
            node = nodes_queue[0]
            nodes_queue = nodes_queue[1:]

            if node:
                vals.append("(" + str(node.key) + ", " + str(node.value) + ")")
                if node.left or node.right:
                    # Append both children to queue
                    # if even one child is not empty
                    nodes_queue.append(node.left)
                    nodes_queue.append(node.right)
            else:
                vals.append("None")

        return "-".join(vals)


if __name__ == "__main__":
    myBST = BST()
    myBST.insert(20, "hello")
    myBST.insert(10, "world")
    myBST[15] = "this"
    myBST[30] = "is"
    myBST[45] = "my"
    myBST[5] = "bst"

    """
                20
            /        \
           10        30
          /  \      /  \
         5   15   None 45

    """

    print(myBST) # 20-10-30-5-15-None-45
    print(myBST[20]) # "hello"

    bstMin = myBST.find_min()
    bstMax = myBST.find_max()
    print(bstMin.key) # 5
    print(bstMax.key) # 45
    print(myBST.find_next_larger(bstMin).key) # 10
    print(myBST.find_next_larger(10)) # 20
    print(myBST.find_next_larger_val(45)) # None

    myBST.insert(4)
    myBST.insert(3)
    myBST.insert(55)
    myBST.insert(50)
    myBST.insert(18)

    print(myBST)

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

    print(myBST.find_next_larger(3).key) # 4
    print(myBST.find_next_larger(4).key) # 5
    print(myBST.find_next_larger(15).key) # 18
    print(myBST.find_next_larger(45).key) # 50
    print(myBST.find_next_larger(55)) # None

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
            N  18     N  55
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
