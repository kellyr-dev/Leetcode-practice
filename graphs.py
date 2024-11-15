import queue

# Basic Theory for Graphs start with BFS and DFS to traversal graphs

# BFS template on Graphs
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

def largestComponents(graph_input):

    largest = 0
    visited = {}
    def dfs(graph, src):

        if src in visited:
            return 0

        visited[src] = True
        count = 1
        for node in graph[src]:
            count = count + dfs(graph, node)

        return count

    for node in graph_input:
        largest = max(largest, dfs(graph_input, node))

    return largest

# ShortestPath without weight
def shortestPath(graph, source, target):

    queue = []  # Queue for making BFS
    queue.append((source, 0))
    visited = {}
    visited[source] = True

    while queue:

        current = queue.pop(0)
        if current[0] == target:
            return current[1]

        distance = current[1]

        for neighbor in graph[current[0]]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
                visited[neighbor] = True

    return -1

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

# 1559. Detect Cycles in 2D Grid (TLE not checked)
def containsCycle(grid):

    cache = {}
    def dfs(grid, i, j, startPoint, cache, count):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return False

        key = (i,j)
        if key in cache:
            if key == (startPoint[0], startPoint[1]) and count >= 4:
                    return True

            return False

        cache[key] = True
        if grid[i][j] != grid[startPoint[0]][startPoint[1]]:
            return False

        return (dfs(grid, i+1, j, startPoint, cache, count+1) or dfs(grid, i-1, j, startPoint, cache, count+1)
    or dfs(grid, i, j+1, startPoint, cache, count+1) or dfs(grid, i, j-1, startPoint, cache, count+1))


    for i in range(len(grid)):
        for j in range(len(grid[0])):
            visited = {}
            startPoint = (i,j)
            count = 0
            if dfs(grid, i, j, startPoint, visited, count):
                return True
    return False

# Topological Sort
def topolicalOrder(edges):

    khan = {}
    graph = {}

    # initialize Khan for all nodes
    for node in edges:
        khan[node[0]] = 0
        khan[node[1]] = 0
        if node[0] in graph:
            graph[node[0]].append(node[1])
        else:
            graph[node[0]] = [node[1]]

        if node[1] not in graph:
            graph[node[1]] = []

    # getting in-degree node
    for node in edges:
        khan[node[1]] += 1

    # initialize the queue with only in-degree nodes
    queue = []

    for node in khan:
        if khan[node] == 0:
            queue.append(node)

    print(khan)
    print(graph)
    result = []
    while queue:
        current = queue.pop(0)
        print(f"current: {current}")
        result.append(current)

        for neighbor in graph[current]:
            print(f"neig: {neighbor}")
            khan[neighbor] -= 1
            if khan[neighbor] == 0:
                queue.append(neighbor)

    return result

# 127. Word Ladder
def ladderLength(beginWord, endWord, wordList):

    wordList.index(0, wordList)
    #building Graph
    for i in range(len(wordList)):
        current_word = wordList[i]
        globalMin = float('-inf')
        for j in range(len(wordList)):

            graphOfmin = {}
            if i != j:
                word = wordList[j]
                count = 0
                for k in range(len(word)):
                    if current_word[k] != word[k]:
                        count+=1

                globalMin = min(count, globalMin)
                graphOfmin[word] = count






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

if __name__ == '__main__':
    # Strategy for matrix algorithms

    grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
    edges = [4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
    n = 5
    m = 3
    s = 1
    word = "applepenapple"
    wordDict = ["apple", "pen"]
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(ladderLength(beginWord, endWord, wordList))
