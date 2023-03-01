# Структура узла дерева
class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


counter = 0


# Функция для получения левой высоты
# бинарного дерева
def left_height(node):
    global counter
    ht = 0
    counter += 1
    while node:
        ht += 1
        counter += 2
        node = node.left
        counter += 2

    # Возвращаем полученную левую высоту
    return ht


# Функция для получения правой высоты
# бинарного дерева
def right_height(node):
    global counter
    ht = 0
    counter += 1
    while node:
        ht += 1
        counter += 2
        node = node.right
        counter += 2

    # Вернуть полученную правую высоту
    return ht


# Функция для получения количества узлов
# в полном бинарном дереве
def total_nodes(root):
    global counter
    # База
    if root is None:
        return 0

    # Найдите левую высоту и
    # правильная высота
    lh = left_height(root)
    counter += 1
    rh = right_height(root)
    counter += 1

    # Если высота слева и справа
    # равны, то возвращаем 2^высота(1<<высота) -1
    if lh == rh:
        return (1 << lh) - 1
    counter += 2

    # В противном случае рекурсивный вызов
    return 1 + total_nodes(root.left) + total_nodes(root.right)


# Сложность T(N) = 2*T(N/2)
#
#
def main():
    global counter

    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(9)
    root.right.right = node(8)
    root.left.left.left = node(6)
    root.left.left.right = node(7)

    print(total_nodes(root))
    print(counter)


if __name__ == '__main__':
    main()
