class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.count = 0
        self.leafs = 0

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.right)
        print(node.data)
        self.show_tree(node.left)

    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def counter(self, node):
        if node is None:
            return None

        self.counter(node.left)
        self.count += 1
        self.counter(node.right)

        return self.count

    def leaf_counter(self, node):
        if node is None:
            return None

        if node.left is None and node.right is None:
            self.leafs += 1

        self.leaf_counter(node.left)
        self.leaf_counter(node.right)

        return self.leafs


v = [10, 5, 7, 16, 13, 2, 20]

t = Tree()
for x in v:
    t.append(Node(x))

# t.show_tree(t.root)
t.show_wide_tree(t.root)

print(t.counter(t.root))
print(t.leaf_counter(t.root))
