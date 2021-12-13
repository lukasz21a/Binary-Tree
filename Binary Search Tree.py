from collections import deque


class Node:
    """
    class to build a Binary Search Tree.
    """
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        """
        Properly distributes the values so the tree is a Binary Search Tree.
        """
        if not self.data:
            self.data = data
            return None
        if self.data == data:
            return None
        if data < self.data:
            if self.left:
                self.left.insert(data)
                return None
            self.left = Node(data)
            return None
        if self.right:
            self.right.insert(data)
            return None
        self.right = Node(data)

    def get_min(self):
        """
        Get the minimal value in the tree.
        """
        current = self
        while current.left:
            current = current.left
        return current.data

    def get_max(self):
        """
        Get the maximum value in the tree.
        """
        current = self
        while current.right:
            current = current.right
        return current.data

    def exists(self, data):
        """
        Check if a value exists in the tree.
        """
        if data == self.data:
            return True
        if data < self.data:
            if self.left is None:
                return False
            return self.left.exists(data)
        if self.right is None:
            return False
        return self.right.exists(data)

    def preorder(self, val):
        """
        Returns the values of a BST as a list in a preorder way.
        """
        if self.data:
            val.append(self.data)
        if self.left:
            self.left.preorder(val)
        if self.right:
            self.right.preorder(val)
        return val

    def inorder(self, val):
        """
        Returns the values of a BST as a list in a inorder way.
        """
        if self.left:
            self.left.inorder(val)
        if self.data:
            val.append(self.data)
        if self.right:
            self.right.inorder(val)
        return val

    def postorder(self, val):
        """
        Returns the values of a BST as a list in a postorder way.
        """
        if self.left:
            self.left.postorder(val)
        if self.right:
            self.right.postorder(val)
        if self.data:
            val.append(self.data)
        return val


def level_order_traversal(node):
    """
    Returns the values of a BST as a list in a level order traversal way.
    """
    dq = deque()
    dq.append(node)
    result = list()
    while dq:
        current = dq.popleft()
        result.append(current.data)
        if current.left:
            dq.append(current.left)
        if current.right:
            dq.append(current.right)
    return result


nums = [16, 12, 21, 4, 14, 10, 20, 72, 3, 15]
bst = Node()
for num in nums:
    bst.insert(num)

print("level order traversal")
print(level_order_traversal(bst))
print()

print("preorder:")
print(bst.preorder([]))
print()

print("inorder:")
print(bst.inorder([]))
print()

print("postorder:")
print(bst.postorder([]))
print()

print("14 exists:", bst.exists(14))
print()
print("1 exists:", bst.exists(1))
print()

print("get the min value:", bst.get_min())
print()
print("get the max value:", bst.get_max())
