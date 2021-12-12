from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def level_order_traversal(node):
    dq = deque()
    dq.append(node)
    result = list()
    while dq:
        current = dq.popleft()
        result.append(current.data)
        # or without the return statement just print the results
        # print(current.data, end=' ')
        if current.left:
            dq.append(current.left)
        if current.right:
            dq.append(current.right)
    return result


def reverse_tree(node):
    if node:
        node.right, node.left = node.left, node.right
        reverse_tree(node.right)
        reverse_tree(node.left)
        return node


root = Node(3)
root.left = Node(5)
root.right = Node(12)
root.left.left = Node(4)
root.left.right = Node(9)
root.left.right.left = Node(8)
root.left.right.right = Node(10)
root.right.right = Node(11)
root.right.right.left = Node(22)

print(level_order_traversal(root))
rev = reverse_tree(root)
print(level_order_traversal(rev))