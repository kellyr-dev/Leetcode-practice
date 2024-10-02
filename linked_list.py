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
    def detectCycle(self, hennnnnnjjjhhuuuyyuuvcdxzaqwwerdfcvbnkljgghreewwuwad):

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


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(12)
    head.next.next = Node(103)
    head.next.next.next = Node(1004)
    head.next.next.next.next = Node(10005)
    head.next.next.next.next.next = Node(100006)

    # 1 -> 12 - > 103 - > 1004 -> 10005 -> 100006

    solution = Solution()
    result = solution.detectCycle(head)
    if result is not None:
        print((result.val))
    else:
        print(result)
