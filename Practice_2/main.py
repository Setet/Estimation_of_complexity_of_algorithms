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

    def show_t(self, node):
        if node is None:
            return

        self.show_t(node.right)
        print(node.data)
        self.show_t(node.left)

    def show_wide_t(self, node):
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

    def count(self, node):
        if node is None:
            return None

        self.count(node.left)
        self.count += 1
        self.count(node.right)

        return self.count

    def cosv_count(self, node):
        if node is None:
            return None

        self.node_l(node.left)
        self.count += 1
        self.node_r(node.right)

        return self.count

    def node_l(self, node):
        if node is None:
            return None

        self.node_l(node.left)
        self.count += 1
        self.node_r(node.right)

    def node_r(self, node):
        if node is None:
            return None

        self.node_l(node.left)
        self.count += 1
        self.node_r(node.right)


v = [9, 4, 6, 11, 10, 1, 10]

t = Tree()
for x in v:
    t.append(Node(x))

# t.show_tree(t.root)
t.show_wide_t(t.root)
print(t.cosv_count(t.root))
