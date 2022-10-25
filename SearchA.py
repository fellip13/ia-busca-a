"""
Integrantes do grupo da atividade prática:
Fellip da Silva Ribeiro                - RA: 11201921507
Thales Cunha de Paixão                 - RA: 11201920276
Paulo Henrique Guilherme Coutinho      - RA: 11201811010
"""


class TreeNode:
    def __init__(self, puzzle, cost, order="N/A"):
        self.puzzle = puzzle
        self.cost = cost
        self.children = []
        self.order = order
        self. parent = None

    def add_child(self, child):
        self.child = child
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level

    def print_tree(self):
        print('  ' * self.get_level() + '|-- ', end='')
        print(f"{self.puzzle} --- {self.cost} --- {self.get_level()} --- {self.order}"
              f"{'°' * int(self.order != 'N/A')}{' --- Resolvido!' * int(self.cost == 0)}")
        if self.children:
            for each in self.children:
                each.print_tree()

    def next_search_node(self, best_node, limit_cost):
        if len(self.children) == 0:
            if self.cost + self.get_level() < best_node.cost + best_node.get_level() and \
                    self.cost + self.get_level() <= limit_cost:
                return self
            return best_node
        else:
            for each in self.children:
                result = each.next_search_node(best_node, limit_cost)
                if result.cost + result.get_level() < best_node.cost + best_node.get_level() and \
                        result.cost + result.get_level() <= limit_cost:
                    best_node = result
            return best_node

    def search_node(self, puzzle):
        if self.puzzle == puzzle:
            return True
        for each in self.children:
            result = False or each.search_node(puzzle)
            if result:
                return result
        return False

    def count_nodes(self, nodes):
        nodes += 1
        if self.children:
            for each in self.children:
                nodes = each.count_nodes(nodes)
        return nodes

    def expanded_nodes(self, nodes_expanded):
        if len(self.children) != 0:
            nodes_expanded += 1
            for each in self.children:
                nodes_expanded = each.expanded_nodes(nodes_expanded)
        return nodes_expanded


def possible_moves_zero(position_zero):
    moves_zero = [[-1, 0], [1, 0], [0, 1], [0, -1]]  # [cima, baixo, direita, esquerda]
    if (position_zero[1] == 0):  # borda esquerda
        moves_zero.pop(3)
    if (position_zero[1] == 2):  # borda direita
        moves_zero.pop(2)
    if (position_zero[0] == 2):  # borda inferior
        moves_zero.pop(1)
    if (position_zero[0] == 0):  # borda superior
        moves_zero.pop(0)
    return moves_zero


def position_zero(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                return [i, j]


def cost(matriz):
    cost = 0
    positions = [[2, 2], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1]]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            value = matriz[i][j]
            if (value == 0):
                continue
            position = positions[value]
            cost += abs(i - position[0]) + abs(j - position[1])
    return cost


def apply_move(matriz, move, position_zero):
    i_new_zero = position_zero[0] + move[0]
    j_new_zero = position_zero[1] + move[1]
    number_to_swap = matriz[i_new_zero][j_new_zero]
    matriz[position_zero[0]][position_zero[1]] = number_to_swap
    matriz[i_new_zero][j_new_zero] = 0
    return matriz


def solve_puzzle(node, root, previous):
    previous += 1
    node.order = previous
    zero_position = position_zero(node.puzzle)
    moves_zeros = possible_moves_zero(zero_position)
    for move in moves_zeros:
        new_puzzle = [node.puzzle[0].copy(), node.puzzle[1].copy(), node.puzzle[2].copy()]
        new_puzzle = apply_move(new_puzzle, move, zero_position)
        cost_new_puzzle = cost(new_puzzle)
        if root.search_node(new_puzzle) == False:
            newNode = TreeNode(new_puzzle, cost_new_puzzle)
            node.add_child(newNode)
    next_node = root.next_search_node(newNode, node.get_level() + node.cost)
    if next_node.cost != 0 and root.count_nodes(0) <= 10000:
        solve_puzzle(next_node, root, previous)


def generate_puzzle():
    return [[int(number) for number in input(f'Digite a {times}º linha do puzzle separado por vírgula (três valores): ') \
        .split(',')] for times in [1,2,3]]

def main():
    puzzle = generate_puzzle()
    print(puzzle)
    cost_puzzle = cost(puzzle)
    root = TreeNode(puzzle=puzzle, cost=cost_puzzle)
    solve_puzzle(node=root, root=root, previous=0)
    print("\nÁrvore expandida: \n")
    root.print_tree()
    print("\nEstrutura da árvore expandida acima: ")
    print("|-- Puzzle configuration --- Cost --- Depth --- Expansion Order")
    print("""    |-- Filho
        |-- neto
        |-- neto
    |-- Filho
    |-- Filho""")
    print("\nNós criados (incluindo o nó raiz): ", root.count_nodes(0))
    print("Nós expandidos (incluindo o nó raiz): ", root.expanded_nodes(0))


if __name__ == '__main__':
    main()
    pass
