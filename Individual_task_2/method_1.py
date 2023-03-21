import random


def find_clique(graph):
    clique = []
    vertices = list(graph.keys())
    rand = random.randrange(0, len(vertices), 1)
    clique.append(vertices[rand])
    for v in vertices:
        if v in clique:
            continue
        isNext = True
        for u in clique:
            if u in graph[v]:
                continue
            else:
                isNext = False
                break
        if isNext:
            clique.append(v)

    return sorted(clique)


def main():
    graph = dict()
    graph['0'] = ['1', '4', '3']
    graph['1'] = ['0', '3', '4']
    graph['2'] = ['4', '5']
    graph['3'] = ['0', '1', '4']
    graph['4'] = ['0', '1', '2', '3', '5', '7']
    graph['5'] = ['2', '4', '8']
    graph['6'] = ['7']
    graph['7'] = ['6', '4', '8']
    graph['8'] = ['7', '5']

    clique = find_clique(graph)
    print('Размер макс.клики: ', len(clique))


if __name__ == "__main__":
    main()
