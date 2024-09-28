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

if __name__ == '__main__':

    head = Node(3)
    aux1 = Node(2)
    aux2 = Node(100)
    aux3 = Node(-4)

    head.next = aux1
    aux1.next = aux2
    aux2.next = aux3

    solution = Solution()
    result = solution.middleNode(head)
    print(result.val)

    '''
        sol = Solution()
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        print("LinkedList has cycle: " + str(sol.hasCycle(head)))
        
        head.next.next.next.next.next.next = head.next.next
        print("LinkedList has cycle: " + str(sol.hasCycle(head)))
        
        head.next.next.next.next.next.next = head.next.next.next
        print("LinkedList has cycle: " + str(sol.hasCycle(head)))
    '''
