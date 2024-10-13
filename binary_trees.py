# Node class for a binary tree node
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


# generate tree from list
def deserialize(lst):
    if len(lst) == 0:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        if i + 1 < len(lst) and lst[i + 1] is not None:
            current.right = TreeNode(lst[i + 1])
            queue.append(current.right)
        i += 2
    return root

def print_bfs(root):
    bfs_queue = list()
    bfs_queue.append(root)

    while (len(bfs_queue) > 0):
        current = bfs_queue.pop(0)
        print(current.value)
        if current.left != None:
            bfs_queue.append(current.left)
        if current.right != None:
            bfs_queue.append(current.right)

def find_min_value(root):
    if root == None:
        return -1

    queuIn = list()
    queuIn.append(root)
    min = float('inf')

    while (len(queuIn) > 0):
        current = queuIn.pop(0)
        if current.value < min:
            min = current.value

        if current.left != None:
            queuIn.append(current.left)

        if current.right != None:
            queuIn.append(current.right)

    return min

def find_min_recursive(root):
    if root == None:
        return float('inf')

    return min(root.value, find_min_recursive(root.left), find_min_recursive(root.right))

def max_sum_path(root):
    if root == None:
        return 0

    return max(root.value + max_sum_path(root.left), root.value + max_sum_path(root.right))

def longest_path_binary(root):
    if root == None:
        return 0

    return max(1 + longest_path_binary(root.left), 1 + longest_path_binary(root.right))

def lowest_common_ancestor(root, value1, value2):
    list_value1 = bfs(root, value1)  # O(N)
    list_value2 = bfs(root, value2)  # O(N)

    print(list_value1)
    print(list_value2)

    tam_1 = len(list_value1) - 1
    tam_2 = len(list_value2) - 1

    # O(N)

    # O(3N)
    if len(list_value2) > len(list_value1):
        for i in range(tam_2 - 1, 0, -1):
            if list_value2[i] == list_value1[tam_1]:
                if i > 0:
                    if list_value2[i - 1] == list_value1[tam_1 - 1]:
                        return list_value1[tam_1 - 1]
    else:
        for i in range(tam_1 - 1, 0, -1):
            if list_value1[i] == list_value2[tam_2]:
                if i > 0:
                    if list_value1[i - 1] == list_value2[tam_2 - 1]:
                        return list_value2[tam_2 - 1]

def bfs(root, value):
    queque_bfs = list()
    queue_return = list()

    if root.value == value:
        queue_return.append(value)
        return queue_return

    queque_bfs.append(root)

    while (len(queque_bfs) > 0):
        current = queque_bfs.pop(0)
        queue_return.append(current.value)

        if current.value == value:
            return queue_return

        if current.left != None:
            queque_bfs.append(current.left)

        if current.right != None:
            queque_bfs.append(current.right)

    return queue_return

# 102. Binary Tree Level Order Traversal
def traversebfs(root):
    queue = []
    queue.append(root)

    res = []
    while len(queue) > 0:

        currenLevel = []
        levelSize = len(queue)

        for i in range(levelSize):  # 1, #2, #4
            current = queue.pop(0)
            currenLevel.append(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        print(currenLevel)
        res.append(currenLevel)

    return res

# 107. Binary Tree Level Order Traversal II
def levelOrderBottom(root):
    if not root:
        return []

    queue = []
    queue.append(root)

    pre_result = []
    while queue:
        level = len(queue)
        aux = []

        for i in range(level):
            currentNode = queue.pop(0)
            aux.append(currentNode.value)

            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)

        pre_result.insert(0, aux)

    print(pre_result)
    return pre_result

# 103. Binary Tree Zigzag Level Order Traversal
def zigzagLevelOrder(root):

    if not root:
        return []

    toleft = False
    toright = True

    queue = []
    queue.append(root)
    result = []

    while queue:
        aux = []
        levelSize = len(queue)
        print(f"toRight--> {toright}")
        print(f"toLeft--> {toleft}")

        for i in range(levelSize):
            currentNode = queue.pop(0)

            if toright == True and toleft == False:
                aux.append(currentNode.value)

            if toright == False and toleft == True:
                aux.insert(0, currentNode.value)

            if currentNode.left is not None:
                queue.append(currentNode.left)

            if currentNode.right is not None:
                queue.append(currentNode.right)

        result.append(aux)
        toleft = not toleft
        toright = not toright

    return result

# 637. Average of Levels in Binary Tree
def averageOfLevels(root):

    queue = []
    queue.append(root)
    result = []

    while queue:
        levelSize = len(queue)
        suma = 0

        for _ in range(levelSize):
            current = queue.pop(0)
            suma = suma + current.value

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        average = suma / levelSize
        result.append(average)

    return result

# 111. Minimum Depth of Binary Tree
def minDepth(root):

    if root is None:
        return 0

    queue = []
    queue.append(root)

    minDepth = 1
    while queue:
        levelSize = len(queue)

        for _ in range(levelSize):
            current = queue.pop(0)

            if current.left is None and current.right is None:
                return minDepth

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        minDepth += 1

    return minDepth

# 113. Path Sum II
def pathSum(root, targetSum):

    allPaths = []
    localPath = []

    def local_path(root, target, localPath, allPaths):

        if root is None:
            return

        localPath.append(root.value)

        if root.value == target and root.left is None and root.right is None:
            allPaths.append(list(localPath))
        else:
            local_path(root.left, target - root.value, localPath, allPaths)
            local_path(root.right, target - root.value, localPath, allPaths)

        localPath.pop()

    local_path(root, targetSum, localPath, allPaths)
    return allPaths

# 129. Sum Root to Leaf Numbers
def sumaRootToLeaf(root):

    def dfs(root, suma):

        if root == None:
            return 0

        suma = suma * 10 + root.value

        if root.left == None and root.right == None:
            return suma

        return dfs(root.left, suma) + dfs(root.right, suma)

    return dfs(root, 0)

# 116. Populating Next Right Pointers in Each Node
def populatingNextRightPointer(root):

    cola = []
    result = []
    cola.append(root)
    previousNode = None

    while cola:

        levelSize = len(cola)
        previousNode = None
        for i in range(levelSize):
            currenNode = cola.pop(0)

            if previousNode:
                previousNode.next = currenNode

            previousNode = currenNode
            print(f"CurrentNode: {currenNode.value}")
            print(f"PreviousNode: {previousNode.value}")

            if currenNode.left != None:
                cola.append(currenNode.left)
            if currenNode.right != None:
                cola.append(currenNode.right)

    return root

# 199. Binary Tree Right Side View
def rightSideView(root):

    if root is None:
        return None

    res = []
    queue = []
    queue.append(root)

    while queue:
        levelSize = len(queue)
        for i in range(levelSize):
            currentNode = queue.pop(0)

            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)

            if (i + 1) == levelSize:
                res.append(currentNode.value)
    return res

# 938. Range Sum of BST
def rangeSumBST(root, low, high):

    if root is None:
        return None

    queue = [root]
    currentNode = None
    suma = 0

    while queue:

        levelsize = len(queue)
      #  print(levelsize)

        for i in range(levelsize):
            currentNode = queue.pop(0)
          #  print(currentNode.value)
            if currentNode.value >= low and currentNode.value <= high:
                suma += currentNode.value

            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)

    return suma

# 112. Path Sum
def hasPathSum(root, targetSum):

    if root is None:
        return False
    def helper(root, target):

        if root is None:
            return False

        if root.left is None and root.right is None and root.value == target:
            return True

        leftSide = helper(root.left, target-root.value) # making calls for the left child
        rightSide = helper(root.right, target-root.value) # making calls for the right child

        return leftSide or rightSide

    result = helper(root, targetSum)
    return result

# 129. Sum Root to Leaf Numbers
def sumPathTotal(root):

    paths = []
    def dfs(root, localPath, globalPath):

        if root is None:
            return 0

        localPath.append(str(root.value))

        if root.right is None and root.left is None:
            globalPath.append(list(localPath))

        dfs(root.left, localPath, globalPath)
        dfs(root.right, localPath, globalPath)

        del localPath[-1]

    dfs(root, [], paths)

    print(f"after: {paths}")
    result = 0
    for path in paths:
        number = "".join(path)
        result = result + int(number)
    return result

# Find if a sequence is present in a root-to-lead path in a given tree
def findPath(root, sequence):
    def dfs(root, index):

        if index >= len(sequence):
            return False

        if root is None:
            return False

        if root.value == sequence[index]:
            if root.left is None and root.right is None and index == len(sequence)-1:
                return True
            else:
                return dfs(root.left, index+1) or dfs(root.right, index+1)
        else:
            return False

    result = dfs(root, 0)
    return result

# Count all paths that sum a target
def countPathSum(root, targetSum):
    def dfs(root, target):

        if root is None:
            return 0

        if root.value == target and root.left is None and root.right is None:
            return 1
        else:
            return dfs(root.left, target - root.value) + dfs(root.right, target - root.value)

    result = dfs(root, targetSum)
    return result

# 437. Path Sum III (not checked)
def pathSumIII(root, targetSum):

    result = 0

    # make dfs
    # keep tracking and adding elem to the sum
    # count all sum == target
    def dfs(root, target):

        print(f"target: {target}")
        if root is None:
            return 0

        if root.value == target:
            return 1 + dfs(root.left, target) + dfs(root.right, target)
        else:
            return (dfs(root.left, target - root.value) + dfs(root.left, target)
                    + dfs(root.right, target) + dfs(root.right, target-root.value))

    result = dfs(root, targetSum)
    return result

# 543. Diameter of Binary Tree
def diameterOfBinaryTree(root):


    result = []
    def dfsHeight(root):

        if root is None:
            return 0

        leftHeight = dfsHeight(root.left)
        rightHeight = dfsHeight(root.right)

        localDiameter = leftHeight + rightHeight
        result.append(localDiameter)

        return 1 + max(leftHeight, rightHeight)

    dfsHeight(root)
    print(f"result: {result}")
    return max(result)


if __name__ == '__main__':
    lst = [1,2,3,None,4,5,6]
    low = 6
    high = 10
    root = deserialize(lst)
    key = 22
    print(diameterOfBinaryTree(root))
    a = [3, 2, 1, 5, 4, 6]
