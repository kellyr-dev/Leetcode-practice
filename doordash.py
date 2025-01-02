import heapq

# 1790. Check if One String Swap Can Make Strings Equal
def areAlmostEqual(s1, s2):

    if s1 == s2:
        return True  # if strings are equal then swaping is not required
    if sorted(s1) != sorted(s2):
        return False  # if sorted s1 and s2 are not equal then swaping will not make strings equal


    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    if count != 2:  # the count should be 2, then only we can do at most one string swap
        return False

    return True


# 286. Walls and Gates (NOT FINISHED)
def wallsAndGates(rooms):
    def dfs(i, j):

        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]):
            return 2147483647

        if rooms[i][j] == 0:
            return 1

        if rooms[i][j] == -1:
            return 2147483647

        key = (i, j)
        if key in visited:
            return visited[key]
        print(f"rooms[i][j]: {rooms[i][j]}")

        visited[key] = rooms[i][j]

        return 1 + min(dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1))

    visited = {}
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):

            key = (i, j)

            if rooms[i][j] != 0 and rooms[i][j] != -1:
                #print(f"(i,j): {(i, j)}")
                #print(f"rooms[i][j]: {rooms[i][j]}")
                #print(f"{rooms}")
                value = dfs(i, j)
                print(f"value: {value}")
                rooms[i][j] = value
                visited[key] = value

# 1779. Find Nearest Point That Has the Same X or Y Coordinate
def nearestValidPoint(x, y, points):

    minHeap = []
    i = 0
    for point in points:

        if point[0] == x or point[1] == y:
            value = abs(point[0] - x) + abs(point[1] - y)
            key = (value, i)
            minHeap.append(key)

        i += 1

    if len(minHeap) < 1:
        return -1

    heapq.heapify(minHeap)
    result = heapq.heappop(minHeap)
    return result[1]

#

if __name__ == '__main__':

    rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

    #s1 = "bank"
    #s2 = "kanb"
    #s1 = "abcd"
    #s2 = "dcba"
    s1 = "q g q eg"
    s2 = "g q g eq"
    print(areAlmostEqual(s1,s2))