
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


def longest_path_binary_tree(root):
    print(root)
    pass

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

    return max(1 + longest_path_binary(root.left), 1+longest_path_binary(root.right))


def lowest_common_ancestor(root, value1, value2):

    list_value1 = bfs(root, value1) # O(N)
    list_value2 = bfs(root, value2) # O(N)

    print(list_value1)
    print(list_value2)

    tam_1 = len(list_value1)-1
    tam_2 = len(list_value2)-1

    # O(N)

    # O(3N)
    if len(list_value2) > len(list_value1):
        for i in range(tam_2-1, 0, -1):
            if list_value2[i] == list_value1[tam_1]:
                if i > 0:
                    if list_value2[i-1] == list_value1[tam_1-1]:
                        return list_value1[tam_1-1]
    else:
        for i in range(tam_1-1, 0, -1):
            if list_value1[i] == list_value2[tam_2]:
                if i > 0:
                    if list_value1[i-1] == list_value2[tam_2-1]:
                        return list_value2[tam_2-1]


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

if __name__ == '__main__':
    #lst = [1, 2, 3, None, None, None, 4]
    lst = [5, 2, 7, None, None, 4, 8, None, None, None, 9]
    #lst = [5, 10, 30, 25, 100, 85, 30]
    root = deserialize(lst)
    #print(find_min_value(root))
    #print_bfs(root)
    #print(max_sum_path(root))
    print(lowest_common_ancestor(root, 2, 9))
    #a = [3, 2, 1, 5, 4, 6]

