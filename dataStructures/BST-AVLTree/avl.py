from bst import BSTNode, BST

class AVLNode(BSTNode):
    def __init__(self, key, value):
        super().__init__(key, value)
        self.height = 0

class AVL(BST):
    def insert(self, key, value):
        # current is newly inserted node
        current = super().insert(key, value)
        self.rebalance(current)

    def delete(self, input_node):
        deleted = super().delete(input_node)
        self.rebalance(deleted.parent)

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def update_height(self, node):
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        node.height = max(left_height, right_height) + 1

    def get_load_balance(self, node):
        right_height = self.height(node.right)
        left_height = self.height(node.left)

        # 0 means right and left are balanced
        # -x means left is taller by x
        # +x means right is taller by x
        return  right_height - left_height

    def rebalance(self, node):
        """
        Case 1: straight path
            A
           / \
          B   y
         / \
        C   x

        Case 2: kinked path
            A
           / \
          B   y
           \
            C
        """
        current = node
        while current:
            self.update_height(current)
            load_balance = self.get_load_balance(current)

            # left is taller
            if load_balance < -1:
                # Case 1: straight path
                # (left-heavy child's left child is taller)
                if self.height(current.left.left) >= \
                        self.height(current.left.right):
                    self.rotate_right(current)

                # Case 2: kinked path
                else:
                    self.rotate_left(current.left)
                    self.rotate_right(current)

            # right is taller
            elif load_balance > 1:
                # Case 1: straight path
                # (right-heavy child's right child is taller)
                if self.height(current.right.right) >= \
                        self.height(current.right.left):
                    self.rotate_left(current)

                # Case 2: kinked path
                else:
                    self.rotate_right(current.right)
                    self.rotate_left(current)

            current = current.parent

    def rotate_right(self, node):
        temp = node.left
        temp.parent = node.parent

        if node.parent is None:
            self.root = temp
        else:
            if node.parent.right is node:
                node.parent.right = temp
            elif node.parent.left is node:
                node.parent.left = temp

        node.left = temp.right
        if temp.right:
            temp.right.parent = node

        temp.right = node
        node.parent = temp

        self.update_height(node)
        self.update_height(temp)

    def rotate_left(self, node):
        temp = node.right
        temp.parent = node.parent

        if node.parent is None:
            self.root = temp
        else:
            if node.parent.right is node:
                node.parent.right = temp
            elif node.parent.left is node:
                node.parent.left = temp

        node.right = temp.left
        if temp.left:
            temp.left.parent = node

        temp.left = node
        node.parent = temp

        self.update_height(node)
        self.update_height(temp)


if __name__ == "__main__":
    myAVL = AVL()
    myAVL[1] = "hello"
    myAVL[2] = "world"
    myAVL[3] = "this"
    myAVL[4] = "is"
    myAVL[5] = "my"
    myAVL[6] = "avl"

    print(myAVL)

    myAVL.delete(2)
    print(myAVL)
    
    myAVL.delete(6)
    print(myAVL)

    myAVL[7] = "another"
    myAVL[8] = "key/value"
    myAVL[9] = "pari"
    myAVL[10] = "inserted"
    print(myAVL)
    """
           4
         /   \
        3     7
       / \   /  \
      1   N 5    9
                /  \
               8   10
    """

    myAVL[11] = "is"
    myAVL[12] = "it"
    myAVL[13] = "still"
    myAVL[14] = "balanced"
    print(myAVL)
    """
             9
          /     \
         4      11
       /   \    /  \
      3     7  10   13
     / \   / \     /  \
    1   N 5   8   12  14
    """
