import heapq
import queue
from string import ascii_letters
from typing import List


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

    for i in range(len(grid)):  # [1,1,0,0,0] =
        for j in range(len(grid[0])):

            key = (i, j)
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

        key = (i, j)
        if key in visited:
            return 0

        visited[key] = True

        if grid[i][j] == 1:
            return 1 + dfs(grid, i + 1, j) + dfs(grid, i - 1, j) + dfs(grid, i, j + 1) + dfs(grid, i, j - 1)
        else:
            return 0

    for i in range(row):
        for j in range(col):
            maxArea = max(maxArea, dfs(grid, i, j))

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

        key = (i, j)
        if key in visited:
            return

        visited[key] = True

        if image[i][j] == color:
            return

        if image[i][j] == origin:
            image[i][j] = color
            dfs(image, i - 1, j)
            dfs(image, i + 1, j)
            dfs(image, i, j - 1)
            dfs(image, i, j + 1)

        return

    dfs(image, sr, sc)

    return image


# 1559. Detect Cycles in 2D Grid (TLE not checked)
def containsCycle(grid):
    cache = {}

    def dfs(grid, i, j, startPoint, cache, count):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return False

        key = (i, j)
        if key in cache:
            if key == (startPoint[0], startPoint[1]) and count >= 4:
                return True

            return False

        cache[key] = True
        if grid[i][j] != grid[startPoint[0]][startPoint[1]]:
            return False

        return (dfs(grid, i + 1, j, startPoint, cache, count + 1) or dfs(grid, i - 1, j, startPoint, cache, count + 1)
                or dfs(grid, i, j + 1, startPoint, cache, count + 1) or dfs(grid, i, j - 1, startPoint, cache,
                                                                            count + 1))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            visited = {}
            startPoint = (i, j)
            count = 0
            if dfs(grid, i, j, startPoint, visited, count):
                return True
    return False


# [Topological Sort]
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

# 207. Course Schedule
def canFinish(numCourses, prerequisites):
    if len(prerequisites) <= 1:
        return True

    graph = {}
    khan = {}
    queue = []

    for pre in prerequisites:
        if pre[0] in graph:
            graph[pre[0]].append(pre[1])
        else:
            graph[pre[0]] = [pre[1]]

        if pre[1] not in graph:
            graph[pre[1]] = []

    for node in prerequisites:
        if node[1] in khan:
            khan[node[1]] += 1
        else:
            khan[node[1]] = 1

    for key in graph:
        if key not in khan:
            queue.append(key)

    print(f"graph: {graph}")
    print(f"khan: {khan}")
    print(f"queue: {queue}")

    if len(queue) == 0:
        return False

    while queue:
        current = queue.pop()

        for node in graph[current]:

            khan[node] -= 1
            if khan[node] == 0:
                queue.append(node)

    for node in khan:
        if khan[node] > 0:
            return False

    #
    return True


# [Dijkstra]
    # step 1:   Maintain a set of processed nodes
    # step 1.1: Building the Graph
    # step 2:   Initialize nodes with distance value = Inf, except Source
    # step 3:   Pick min value vertex which is not already processed
    # step 4:   Included selected node in processed set
    # step 5:   Update all adjacent Node distances
    # step 6:   If (new_distance < old_distance) then update else skip

def DjkstraAlgo(points, src, dst):

    # Step 1 Set for processing nodes
    visited = set()

    graph = {}
    # Step 1.1 Graph for processing vertices for each node
    for i in range(len(points)):
        if points[i][0] not in graph:
            graph[points[i][0]] = [(points[i][1], points[i][2])]
        else:
            graph[points[i][0]].append(points[i][1], points[i][2])

        if points[i][1] not in graph:
            graph[points[i][1]] = []

    # Step 2: Initialize nodes with distance values in 0 and Inf
    min_heap = [(0,src)]
    for key in graph:
        if key != src:
            aux_key = (key, float('inf'))
            heapq.heappush(min_heap, aux_key)

    while len(min_heap) < len(visited):

        current = heapq.heappop(min_heap)

        if current[1] not in visited:
            visited.add(current[1])

        for neighbord in graph[current[1]]:




# 1584. Min Cost to Connect All Points
def minCostConnectPoints(points):

    # Step 1 bulding the initial graph
    visited = {}
    graph = {}
    queue = []
    result = 0

    source = (points[0][0], points[0][1])
    visited[source] = True

    for j in range(1, len(points)):
        key = (points[j][0], points[j][1])
        val = abs(points[0][0] - points[j][0]) + abs(points[0][1] - points[j][1])
        graph[key] = val

    # Step 2 building the initial queue
    for node in graph:
        key = (graph[node], node)
        heapq.heappush(queue, key)

    # BFS from source
    while len(visited) < len(points) and len(queue) > 0:

        # get the minimun guarantee
        currentNode = heapq.heappop(queue)
        if currentNode[1] not in visited:
            result += currentNode[0]
            visited[currentNode[1]] = True

            # building graph for currentNode
            for pointi in points:
                point = (pointi[0], pointi[1])

                if point not in visited and point != currentNode[1]:
                    val = abs(currentNode[1][0] - point[0]) + abs(currentNode[1][1] - point[1])
                    graph[point] = min(graph[point], val)

            # building queue for currentNode
            queue.clear()
            for node in graph:
                key = (graph[node], node)
                heapq.heappush(queue, key)

    return result

# 1584. Min Cost to Connect All Points using [Prim's]
def minCostConnectPointsPrim(points):

    n = len(points)
    visited = set()
    # min_heap = [(d,i)]
    min_heap = [(0,0)]
    result = 0

    while len(visited) < n:

        key = heapq.heappop(min_heap)
        if key[1] in visited:
            continue
        visited.add(key[1])
        result += key[0]

        for j in range(len(points)):

            if j not in visited:
                val = abs(points[key[1]][0] - points[j][0]) + abs(points[key[1]][1] - points[j][1])
                heapq.heappush(min_heap, (val, j))

        print(min_heap)

    return result

# [Union Find]
# 684. Redundant Connection
def findRedundantConnection(edges):

    return True

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

    grid = [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]
    edges = [4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
    n = 5
    m = 3
    s = 1
    word = "applepenapple"
    wordDict = ["apple", "pen"]
    numCourses = 20
    prerequisites = [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]  # false
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    print(DjkstraAlgo(flights, src, dst))

