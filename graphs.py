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

visited = {}

#  /* Alvin practice
def explore_bfs_tree(graph, node):
    visited = {}
    queue = list()
    queue.append(node)
    visited[node] = 1
    cont_visited = 0

    while (len(queue) > 0):
        current = queue.pop(0)
        print(f"current: ", current)

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

def is_a_tree(graph, visited):
    print(graph)

    # find cycles to return False (condition 1)
    for nodes in graph:
        print(f"node: ", nodes)
        if explore_bfs_tree(graph, nodes) > 1:
            return False

    # find unvisited nodes -> means island or disconnected nodes because BFS never toch it (condition 2)
    for nodis in graph:
        if nodis not in visited:
            return False

    return True

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

def shortest_path(graph, source, target):
    aux = list()  # Queue for making BFS
    distance = 0  # distance is the level in the Graph
    # esta es la clave guardar la distancia del Grafo donde empiezas a iterar
    # esto te da el minimo Path
    # Otro Aproach podria ser ir por todos los caminos y sumar (luego devolver el mas pequeno)
    # Pero seria un poco mas lento ya que probablemente iria por todos varias veces
    aux.append([source, distance])
    visited = {}

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

        for i in range(1, len(current) + 1):

            if current[:i] in wordDict:
                queue.append(current[i:])

    return True


# 1971. Find if Path Exists in Graph (BFS)
def validPath(n, edges, source, destination):
    graph = {}

    for node in edges:
        #   print(node)
        if node[0] in graph:
            graph[node[0]].append(node[1])
        else:
            graph[node[0]] = [node[1]]

        if node[1] in graph:
            graph[node[1]].append(node[0])
        else:
            graph[node[1]] = [node[0]]

    print(graph)
    visited = {}
    queue = []

    if source not in graph:
        return False

    queue.append(source)

    while queue:
        print(f"queue: {queue}")
        current = queue.pop(0)

        if current == destination:
            return True

        if current not in visited:
            visited[current] = True
            for neighbor in graph[current]:
                queue.append(neighbor)

    return False


# 1971. Find if Path Exists in Graph (DFS)
def validPathDFS(n, edges, source, destination):
    graph = {}

    for node in edges:
        #   print(node)
        if node[0] in graph:
            graph[node[0]].append(node[1])
        else:
            graph[node[0]] = [node[1]]

        if node[1] in graph:
            graph[node[1]].append(node[0])
        else:
            graph[node[1]] = [node[0]]

    # for each neighbor in source
    # check if exist a path
    # if return True

    visited = {}

    def dfs(graph, source, destination):
        if source in visited:
            return False

        visited[source] = True

        if source == destination:
            return True

        for node in graph[source]:
            if node not in visited:
                if dfs(graph, node, destination) == True:
                    return True

        return False

    return dfs(graph, source, destination)


# 547. Number of Provinces
def findCircleNum(isConnected):
    graph = {}

    for i in range(len(isConnected)):
        graph[i] = []

    for j in range(len(isConnected)):  # list of ([[1,1,0], [1,1,0], [0,0,1]])
        node = isConnected[j]
        for i in range(len(node)):
            if node[i] == 1 and i != j:
                if i in graph:
                    graph[i].append(j)
                else:
                    graph[i] = [j]

    visited = {}
    count = 0
    queue = []
    print(graph)
    for node in graph:
        if node not in visited:
            count += 1
            visited[node] = True
            queue.append(node)
            while queue:
                current = queue.pop(0)
                visited[current] = True
                for each in graph[current]:
                    if each not in visited:
                        queue.append(each)

    return count


# 1557. Minimum Number of Vertices to Reach All Nodes
def findSmallestSetOfVertices(n, edges):
    graph = {}
    visited = {}
    for node in edges:  # list of ([0,1], [0,2], [2,5], [3,4], [4,2])

        if node[0] in graph:
            graph[node[0]].append(node[1])
        else:
            graph[node[0]] = [node[1]]

        if node[0] not in visited:
            visited[node[0]] = 0

        if node[1] in visited:
            visited[node[1]] += 1
        else:
            visited[node[1]] = 1

    result = []
    for node in visited:
        if visited[node] == 0:
            result.append(node)

    return result

# 200. Number of Islands
def numIslands(grid):

    count = 0
    visited = {}
    print(f"row: {len(grid)}")
    print(f"col: {len(grid[0])}")

    def dfs(grid, row, col):

        if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
            return

        key = (row, col)
        if key in visited:
            return

        visited[key] = True

        if grid[row][col] == "1":
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)

        else:
            return

    for i in range(len(grid)): # [1,1,0,0,0] =
        for j in range(len(grid[0])):

            key = (i,j)
            if grid[i][j] == "1" and key not in visited:
                print(f"key: {key}")
                print(f"visited: {visited}")
                count += 1
                dfs(grid, i, j)

    return count

# 695. Max Area of Island
def maxAreaOfIsland(grid):

    maxArea = 0
    visited = {}

    row = len(grid)
    col = len(grid[0])

    def dfs(grid, i, j):

        if i < 0 or i >= row or j < 0 or j >= col:
            return 0

        key = (i,j)
        if key in visited:
            return 0

        visited[key] = True

        if grid[i][j] == 1:
            return 1 + dfs(grid, i+1, j) + dfs(grid, i-1, j) + dfs(grid, i, j+1) + dfs(grid, i, j-1)
        else:
            return 0

    for i in range(row):
        for j in range(col):
            maxArea = max(maxArea, dfs(grid, i,j))

    return maxArea

# 733. Flood Fill
def floodFill(image, sr, sc, color):

    origin = image[sr][sc]
    row = len(image)
    col = len(image[0])
    visited = {}

    def dfs(image, i, j):

        if i < 0 or i >= row or j < 0 or j >= col:
            return

        key = (i,j)
        if key in visited:
            return

        visited[key] = True

        if image[i][j] == color:
            return

        if image[i][j] == origin:
            image[i][j] = color
            dfs(image, i-1, j)
            dfs(image, i+1, j)
            dfs(image, i, j-1)
            dfs(image, i, j+1)

        return

    dfs(image, sr, sc)

    return image



if __name__ == '__main__':
    # Strategy for matrix algorithms
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

    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

    input_tree = {
        0: [1, 2, 3],
        1: [0],
        2: [0],
        3: [0, 4],
        4: [3]
    }

    n = 5
    m = 3
    edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
    s = 1
    word = "applepenapple"
    wordDict = ["apple", "pen"]
    print(islandPerimeter(grid))
