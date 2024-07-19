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

# 113. Path Sum II
def hasPathSum(root, targetSum):

    allPaths = []
    localPath = []

    def local_path(root, targetSum, localPath):

        if root is None:
            return

        localPath.append(root.value)

        if root.value == targetSum and root.left is None and root.right is None:
            allPaths.append(localPath)
        else:
            local_path(root.left, targetSum - root.value, localPath)
            local_path(root.right, targetSum - root.value, localPath)

        del localPath[-1]

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

    res = list()
    queue = [root]

    currentNode = None
    while queue:

        levelSize = len(queue)

        for i in range(levelSize):
            currentNode = queue.pop(0)
            print(f"currenNode: {currentNode.value}")

            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)
        print(f"CurrenNode al salir: {currentNode.value}")
        res.append(currentNode.value)
    return res


if __name__ == '__main__':
    lst = [1,2,3,None,5,None,4]
    root = deserialize(lst)
    key = 22
    print(rightSideView(root))
    # a = [3, 2, 1, 5, 4, 6]
