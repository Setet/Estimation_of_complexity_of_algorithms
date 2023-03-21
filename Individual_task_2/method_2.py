class Node(object):

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def __repr__(self):
        return self.name


A = Node('0')
B = Node('1')
C = Node('2')
D = Node('3')
E = Node('4')
F = Node('5')
G = Node('6')
H = Node('7')
I = Node('8')

A.neighbors = [B, E, D]
B.neighbors = [A, D, E]
C.neighbors = [E, F]
D.neighbors = [A, B, E]
E.neighbors = [A, B, C, D, F, H]
F.neighbors = [C, E, I]
G.neighbors = [H]
H.neighbors = [G, E, I]
I.neighbors = [H, F]

all_nodes = [A, B, C, D, E, F, G, H, I]


def find_cliques(potential_clique=[], remaining_nodes=[], skip_nodes=[], depth=0):
    if len(remaining_nodes) == 0 and len(skip_nodes) == 0:
        print('Это клика:', potential_clique)
        return 1

    found_cliques = 0
    for node in remaining_nodes:
        new_potential_clique = potential_clique + [node]
        new_remaining_nodes = [n for n in remaining_nodes if n in node.neighbors]
        new_skip_list = [n for n in skip_nodes if n in node.neighbors]
        found_cliques += find_cliques(new_potential_clique, new_remaining_nodes, new_skip_list, depth + 1)

        remaining_nodes.remove(node)
        skip_nodes.append(node)
    return found_cliques

def main():
    total_cliques = find_cliques(remaining_nodes=all_nodes)
    print('Размер макс.клики:', total_cliques)

if __name__ == "__main__":
    main()