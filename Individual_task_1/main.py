class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def minDepth(root):
    # Если у нас только корень дерева
    if root is None:
        return 0

    # Если у нас только одна вершина
    if root.left is None and root.right is None:
        return 1

    # Если левое поддерево равно Null, повторить для правого поддерева
    if root.left is None:
        return minDepth(root.right) + 1

    # Если правое поддерево равно Null, повторяется для левого поддерева
    if root.right is None:
        return minDepth(root.left) + 1

    return min(minDepth(root.left), minDepth(root.right)) + 1


root = Node(1)
root.left = Node(2)
#root.right = Node(3)
#root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
print("Минимальная глубина бинарного дерева: " + str(minDepth(root)))
