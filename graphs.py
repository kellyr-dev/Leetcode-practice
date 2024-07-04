
import queue

# PRACTICE ON GRAPHS FOR CODING INTERVIEWS

# Basic Theory for Graphs start with BFS and DFS to traversal graphs
def bfs(graph, entry):
    queue = []  # queue
    queue.append(entry)
    visited = {}  # set to check if a particular node has been visited

    result = []

    while (len(queue) > 0):
        current = queue.pop(0)

        if current not in visited:
            print(current)
            visited[current] = 1
            result.append(current)
            for neighbor in graph[current]:
                queue.append(neighbor)
        else:
            continue

    return result

def dfs(graph, entry):
    aux = list()
    aux.append(entry)

    while (len(aux) > 0):
        current = aux.pop()
        print(current)
        for neight in graph[current]:
            aux.append(neight)


#  /* Alvin practice
visited = {}
def explore_bfs_tree(graph, node):

    visited = {}
    queue = list()
    queue.append(node)
    visited[node] = 1
    cont_visited = 0

    while (len(queue) > 0):
        current = queue.pop(0)
        print(f"current: ",current)

        for list_ad in graph[current]:
            if list_ad in visited:
                cont_visited += 1
            else:
                visited[list_ad] = 1
                queue.append(list_ad)

        print(f"queue: ", queue)
        print(f"cont_visited:", cont_visited)
        if cont_visited > 1:
            return cont_visited
        else:
            cont_visited = 0

    return cont_visited

def is_a_tree(graph):
    print(graph)

    # find cycles to retur False (condition 1)
    for nodes in graph:
        print(f"node: ", nodes)
        if explore_bfs_tree(graph, nodes) > 1:
            return False

    # find unvisited nodes -> means island or disconnected nodes because BFS never toch it (condition 2)
    for nodis in graph:
        if nodis not in visited:
            return False

    return True


def hasPath(graph, src, tgt):
    if src in visited:
        return False

    visited[src] = True

    if src == tgt:
        return True

    for neighbor in graph[src]:
        if (hasPath(graph, neighbor, tgt)):
            return True

    return False

def traversal(graph_input, srcnode):
    if srcnode in visited:
        # print(f"Already visited:", srcnode)
        return False

    visited[srcnode] = 1

    Stack = []
    Stack.append(srcnode)

    while len(Stack) > 0:
        current = Stack.pop()
        # print(f"current:",current)
        for neighbors in graph_input[current]:
            if neighbors not in visited:
                visited[neighbors] = 1
                Stack.append(neighbors)

    return True

# another way is using recursion

def explore(graph_input, srcnode):
    if srcnode in visited:
        return False

    visited[srcnode] = 1

    for neighbor in graph_input[srcnode]:
        explore(graph_input, neighbor)

    return True

def explore_int(graph_input, srcnode):

    if srcnode in visited:
        return 0

    visited[srcnode] = 1
    cont = 1

    for neighbor in graph_input[srcnode]:
        print(f"neighbor:", neighbor)
        print(graph_input[srcnode])
        cont = cont + explore_int(graph_input, neighbor)

    return cont

# Alvin practice */
def largest_components(graph_input):
    largest = 0
    for node in graph_input:
        print(f"node:", node)
        size = explore_int(graph_input, node)
        if size > largest:
            largest = size

    return largest

def connected_components_cont(graph_input):
    contIterative = 0
    contRecursive = 0
    for node in graph_input:
        # if traversal(graph_input, node):
        #    contIterative += 1

        if explore(graph_input, node):
            contRecursive += 1

    return contRecursive

def count_island(matrix):
    cont = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if explore_traversal(matrix, row, col):
                cont += 1

    return cont

def explore_traversal(grid, x, y):
    if x < 0 or x >= len(grid):
        return False

    if y < 0 or y >= len(grid[0]):
        return False

    if grid[x][y] == 'W':
        return False

    key = str(x) + ',' + str(y)
    print(key)

    if key in visited:
        return False

    visited[key] = 1

    explore_traversal(grid, x - 1, y)
    explore_traversal(grid, x + 1, y)
    explore_traversal(grid, x, y - 1)
    explore_traversal(grid, x, y + 1)

    return True


def shortest_path(graph, source, target):
    aux = list()  # Queue for making BFS
    distance = 0  # distance is the level in the Graph
    # esta es la clave guardar la distancia del Grafo donde empiezas a iterar
    # esto te da el minimo Path
    # Otro Aproach podria ser ir por todos los caminos y sumar (luego devolver el mas pequeno)
    # Pero seria un poco mas lento ya que probablemente iria por todos varias veces
    aux.append([source, distance])

    if source == target:
        return distance

    visited[source] = 1

    while (len(aux) > 0):

        current = aux.pop(0)
        print(current)

        if current[0] == target:
            return current[1]

        distance = current[1]

        for neighbor in graph[current[0]]:
            if neighbor not in visited:
                print(f"neighbor:", neighbor)
                aux.append([neighbor, distance + 1])
                print(f"Queue:", aux)

    return -1


def maximunIsland(matrix):

    maxSize = float('inf')
    visitado = {}
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            size = explore_maxIsland(matrix, row, col, visitado)
            print(f"Size: ", size)
            if size < maxSize and size > 0:
                maxSize =  size

    return maxSize


def explore_maxIsland(matrix, row, col, vistado):

    if row >= len(matrix) or row < 0:
        return 0
    if col >= len(matrix[0]) or col < 0:
        return 0

    key = (row, col)
    if key in vistado:
        return 0

    vistado[key] = 1

    if matrix[row][col] == 0:
        return 0

    size = 1 + explore_maxIsland(matrix, row+1, col, vistado) + explore_maxIsland(matrix, row-1, col, vistado) + explore_maxIsland(matrix, row, col+1, vistado) + explore_maxIsland(matrix, row, col-1, vistado)
    return size

# LeetCode 139 using BFS
def wordBreakBFS(word, wordDict):

    if len(word) == 0:
        return True

    queue = [word]
    visited = {}

    while queue:

        current = queue.pop(0)

        if len(current) == 0:
            return True

        if current in visited:
            continue

        visited[word] = 1


        for i in range(1, len(current)+1):

            if current[:i] in wordDict:
                queue.append(current[i:])

    return True


if __name__ == '__main__':
    # Strategy for matrix algoritmos
    # In a matrix should be nested loop + Traverse

    graph_input_largest = {
        0: [1, 5, 8],
        1: [0],
        2: [3, 4],
        3: [2, 4],
        4: [2, 3],
        5: [0, 8],
        8: [0, 5]
    }

    graph_bfs = {
        'w': ['x', 'v'],
        'x': ['y'],
        'y': ['z'],
        'v': ['z']
    }

    graph_white = {
        'A': ['B', 'D', 'C'],
        'B': ['A', 'E'],
        'C': ['F', 'A'],
        'D': ['A', 'G'],
        'F': ['C', 'G'],
        'G': ['E', 'D', 'F'],
        'E': ['B', 'G']
    }

    graph_or = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]

    grid = [
        [0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,0,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]


    #grid = [
    #    ['W', 'L', 'W', 'W', 'W'],
    #    ['W', 'L', 'W', 'W', 'W'],
    #    ['W', 'W', 'W', 'L', 'W'],
    #    ['W', 'W', 'L', 'L', 'W'],
    #    ['L', 'W', 'W', 'L', 'L'],
    #    ['L', 'L', 'W', 'W', 'W'],
    #]

    input_tree = {
        0: [1, 2, 3],
        1: [0],
        2: [0],
        3: [0, 4],
        4: [3]
    }

    # result = is_a_tree(graph_input)
    # print(count_island(grid))
    n = 5
    m = 3
    edges = [[1,2],[1,3],[3,4]]
    s = 1
    word = "applepenapple"
    wordDict = ["apple", "pen"]
    print(wordBreakBFS(word, wordDict))
