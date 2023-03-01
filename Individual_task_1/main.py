# Функция поиска кратчайшего
# путь между двумя узлами графа
def BFS_SP(graph, start, goal):
    explored = []

    # Очередь на обход
    # график в БФС
    queue = [[start]]

    # Если нужный узел
    # достиг
    if start == goal:
        print("Same Node")
        return

    # Цикл для обхода графа
    # с помощью очереди
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Условие проверки
        # текущий узел не посещается
        if node not in explored:
            neighbours = graph[node]

            # Цикл для перебора
            # соседи узла
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Условие проверки
                # соседний узел является целью
                if neighbour == goal:
                    print("Кратчайший путь из " + start + " в " + goal + " = ", *new_path)
                    return
            explored.append(node)

    # Условие, когда узлы
    # не подключены
    print("Извините, но соединительного пути не существует :(")
    return


if __name__ == "__main__":
    # График с использованием словарей
    graph = {'A': ['B', 'E', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B', 'E'],
             'E': ['A', 'B', 'D'],
             'F': ['C'],
             'G': ['C']}
    BFS_SP(graph, 'A', 'E')
