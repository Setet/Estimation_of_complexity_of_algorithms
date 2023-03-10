MAX = 100

# Сохраняет вершины
store = [0] * MAX

# Граф
graph = [[0 for i in range(MAX)] for j in range(MAX)]

# Степень вершин
d = [0] * MAX


# Функция для проверки, является ли заданный набор
# вершин в массиве store кликой или нет
def is_clique(b):
    # Цикл для всего набора ребер
    for i in range(1, b):
        for j in range(i + 1, b):

            # Если какое-либо ребро отсутствует
            if graph[store[i]][store[j]] == 0:
                return False

    return True


# Функция для нахождения всех размеров
# максимальных кликов
def max_сliques(i, l):
    # Максимальный размер клики
    max_ = 0

    # Проверяем, есть ли вершины из i+1
    # можно вставить
    for j in range(i + 1, n + 1):

        # Добавляем вершину для сохранения
        store[l] = j

        # Если граф не является кликой размера k, то
        # это не может быть кликой, если добавить еще одно ребро
        if is_clique(l + 1):
            # Обновить макс
            max_ = max(max_, l)

            # Проверяем, можно ли добавить еще одно ребро
            max_ = max(max_, max_сliques(j, l + 1))

    return max_


if __name__ == '__main__':
    edges = [[1, 2], [2, 3], [3, 1],
             [4, 3], [4, 1], [4, 2]]
    size = len(edges)
    n = 4
    Answer = True

    for i in range(size):
        graph[edges[i][0]][edges[i][1]] = 1
        graph[edges[i][1]][edges[i][0]] = 1

        d[edges[i][0]] += 1
        d[edges[i][1]] += 1

    print(f"Найти максимальную клику в графе.\nОтвет : ", max_сliques(0, 1))
