class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Solution:

    # 141. Linked List Cycle
    def hasCycle(self, head):

        fast = head
        slow = head

        if fast == None:
            return False

        while fast != None and fast.next != None:

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

    # 876. Middle of the Linked List
    def middleNode(self, head):


        '''
        Naive solution

        iterator = head
        solution = head
        if iterator == None:
            return

        count = 0
        while iterator != None:
            count += 1
            iterator = iterator.next

        middle = int(count / 2)
        index = 0

        while index < middle:
            solution = solution.next
            index += 1

        return solution
        '''


        # two pointer solution
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    # 142. Linked List Cycle II
    def detectCycle(self, head):

        fast = head

        if fast is None:
            return None

        table_hash = {}
        while fast is not None:

            key = (fast, fast.val)

            if key not in table_hash:
                table_hash[key] = True
            else:
                return fast

            fast = fast.next

        return None

    # 234. Palindrome Linked List
    def isPalindrome(self, head):

        stack = []
        aux = head
        iterator = head

        while iterator is not None:
            stack.append(iterator.val)
            iterator = iterator.next

        print(stack)
        while stack and aux is not None:
            value = stack.pop()
            if value != aux.val:
                return False
            aux = aux.next
        return True

    # 206. Reverse Linked List
    def reverseList(self, head):

        current = head
        previous = None

        while current is not None:
            aux = current.next # save current next pointer
            current.next = previous # point to previous
            previous = current # previous move to current
            current = aux # current move to next

        head = previous
        return head

    # 92. Reverse Linked List II (not checked)
    def reverseSubList(self, head, left, right):

        if left == right: # case 1
            return head

        stack = []
        prev = None
        current = head

        while current is not None and current.val != left:
            prev = current
            current = current.next

        iterator = None
        saveLater = None
        newPrev = None
        if current is None: # case 2 (need to reverse whole list)
            return self.reverseList(head)

        iterator = current
        saveLater = current
        newPrev = None

        while iterator is not None and iterator.val != right:
            aux = iterator.next
            iterator.next = newPrev
            newPrev = iterator
            iterator = aux

        if iterator is None: # case 3 (when R does not exist in the list)
            prev.next = newPrev
            saveLater.next = None
        else: # cas3 4 (when R exist in the list)
            if prev is None:
                #(need to check)
                saveLater.next = iterator.next
                iterator.next = newPrev

            else:
                prev.next = iterator
                saveLater.next = iterator.next
                iterator.next = newPrev

        return head

    # 25. Reverse Nodes in k-Group
    def reverseKGroup(self, head, k):



if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(4)
    #head.next.next.next.next.next.next = Node(3)
    #head.next.next.next.next.next.next.next = Node(2)
    #head.next.next.next.next.next.next.next.next = Node(1)
    #head.next.next.next.next.next.next.next.next.next = Node(0)
    # 1 -> 12 - > 103 - > 1004 -> 10005 -> 100006

    solution = Solution()
    result = solution.reverseSubList(head, 1, 2)

    while result is not None:
        print(f"{result.val}")
        result = result.next
