# 1554. Strings Differ by One Character
def differByOne(dict):
    for i in range(len(dict)):  # O(n)

        word = dict[i]
        for j in range(i + 1, len(dict)):
            auxWord = dict[j]
            count = 0
            for k in range(len(auxWord)):
                if word[k] != auxWord[k]:
                    count += 1

                if count >= 2:
                    break

            if count == 1 and len(word) > 1:
                return True

    return False

# 136. Single Number
def singleNumber(nums):
    num = 0
    for value in nums:
        print(f"num: {num} XOR value: {value}")
        num = num ^ value
        print(f"resutl: {num}")

    return num

# 190. Reverse Bits
def reverseBits(n):
    print(n)

# 1091. Shortest Path in Binary Matrix
def shortestPathBinaryMatrix(grid):
    n = len(grid) - 1
    if grid[0][0] == 1 or grid[n][n] == 1:
        return -1

    directions = [(-1, -1), (-1, 0), (0, 1), (1, 0), (0, -1), (1, 1), (-1, 1), (1, -1)]

    key = (0, 0)
    queue = [(key, 1)]  # 1 because is the first distance since grid[0][0] != 0
    visited = set()
    visited.add(key)

    while queue:

        currentPoint = queue.pop(0)
        currentRow = currentPoint[0][0]
        currentCol = currentPoint[0][1]
        distance = currentPoint[1]

        if currentRow == n and currentCol == n:
            return distance

        for pair in directions:

            newRow = pair[0] + currentRow
            newCol = pair[1] + currentCol

            if newRow < 0 or newRow > n or newCol < 0 or newCol > n or grid[newRow][newCol] == 1 or (
            newRow, newCol) in visited:
                continue
            else:
                key = (newRow, newCol)
                visited.add(key)
                queue.append((key, distance+1))

    return -1

# 1257. Smallest Common Region
def findSmallestRegion(regions, region1, regions2):

    root = regions[0][0]

    parentSons = {}
    for region in regions:
        for i in range(1, len(region)):
            parentSons[region[i]] = region[0]

    print(parentSons)
    onlyParentOfRegion1 = {}

    auxRegion1 = region1
    while auxRegion1 != root:
        onlyParentOfRegion1[auxRegion1] = parentSons[auxRegion1]
        auxRegion1 = ""+parentSons[auxRegion1]
        #print(f"auxRegion1: {auxRegion1}")

    print(onlyParentOfRegion1)
    auxRegion2 = region2
    while auxRegion2 != root:
        aux = parentSons[auxRegion2]
        if aux in onlyParentOfRegion1:
            return aux
        auxRegion2 = ""+aux

    return auxRegion2



if __name__ == '__main__':
    # nums = [1,1,2,2,4]
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    regions = [["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]]

    region1 = "Canada"
    region2 = "South America"
    nums = [21,21]

