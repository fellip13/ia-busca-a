#182043765

def moves(position):
    moves = []
    for x in [1, -1]:
        if position[0] + x >= 0 and position[0] + x <= 2:
            moves.append([position[0] + x, position[1]])
        if position[1] + x >= 0 and position[1] + x <= 2:
            moves.append([position[0], position[1] + x])
    return moves

def positionOfZero(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                return [i, j] 

def dist(initial: list, final: list):
    return abs(initial[0] - final[0]) + abs(initial[1] - final[1])

def originalPosition(value):
    positions = [[2,2], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1]]
    return positions[value]

def state(matriz):
    state = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            value = matriz[i][j]
            if (value == 0):
                continue
            position = originalPosition(value)
            d = dist([i, j], position)
            state += d
            #print(f'Value {value} [{i},{j}] original position {position} dist {d}')
    return state

def printMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            value = matriz[i][j]
            print(f'{value}', end = ' ')
        print()
    print()

def readMatriz(file: str):
   with open(file, 'r') as file:
    matriz = [[int(number) for number in line.split(',')] for line in file]
    return matriz

def swap(matriz, first, second):
    aux = matriz[first[0]][first[1]]
    matriz[first[0]][first[1]] = matriz[second[0]][second[1]]
    matriz[second[0]][second[1]] = aux

def main():
    file = 'puzzle.txt'
    puzzle = readMatriz(file)
    
    #printMatriz(puzzle)
    #print(f'Initial state {state(puzzle)}')

    print(state([[1,2,0], [4,8,3], [7,6,5]]))
    print(state([[0,1,2], [4,8,3], [7,6,5]]))
    print(state([[1,8,2], [4,6,3], [7,5,0]]))
    print(state([[1,8,2], [4,6,3], [0,7,5]]))


    maxInterantion = 0
    while(True):
        if (state(puzzle) == 0):
            print("solved")
            break

        if (maxInterantion == 10000):
            print("Unresolvable")
            break
        
        zeroPosition = positionOfZero(puzzle)
        movesOfZero = moves(zeroPosition)

        bestPuzzle = None
        for valuePosition in movesOfZero:
            #print('puzzle')
            #printMatriz(puzzle)
            newPuzzle = [puzzle[0].copy(), puzzle[1].copy(), puzzle[2].copy()]
            swap(newPuzzle, zeroPosition, valuePosition)

            print(state(newPuzzle))
            printMatriz(newPuzzle)
            if bestPuzzle is None or state(newPuzzle) < state(puzzle):
                bestPuzzle = [newPuzzle[0].copy(), newPuzzle[1].copy(), newPuzzle[2].copy()]
            #print(f'Future state {state(newPuzzle)}')
            #printMatriz(newPuzzle)

        puzzle = [bestPuzzle[0].copy(), bestPuzzle[1].copy(), bestPuzzle[2].copy()]
        #print('final')
        #printMatriz(puzzle)
        #print(f'Interaction {maxInterantion}')
        maxInterantion += 1

    '''count = 0
    while(True):
        if (state(puzzle) == 0 or count == 3):
            break
        zeroPosition = positionOfZero(puzzle)
        movesOfZero = moves(zeroPosition)

        bests = dict()
        for valuePosition in movesOfZero:
            if (valuePosition[0] == 0 and valuePosition[1] == 0):
                continue

            d = dist(valuePosition, originalPosition(puzzle[valuePosition[0]][valuePosition[1]]))
            print(f'position: {valuePosition} value: {puzzle[valuePosition[0]][valuePosition[1]]} dist: {d}')
            if d == 0:
                continue
            bests[d] = valuePosition
        
        countX = 0
        best = None
        for k, v in bests.items():
            if countX == 0:
                best = [k, v]
                countX = 1
            else:
                if k < best[0]:
                    best = [k, v]
            
        
        print(f'zero position: {zeroPosition} moves: {movesOfZero} best: {best}')

        aux = puzzle[zeroPosition[0]][zeroPosition[1]]
        puzzle[zeroPosition[0]][zeroPosition[1]] = puzzle[best[1][0]][best[1][1]]
        puzzle[best[1][0]][best[1][1]] = aux

        printMatriz(puzzle)
        count += 1
    print(f'{count}')'''


main()