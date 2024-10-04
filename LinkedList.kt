class LinkedList {

    fun printList(head : ListNode?){

        var iterator = head
        while(iterator != null){
            print("${iterator.value} -> ")
            iterator = iterator.next
        }
        
    }

    // 206. Reverse Linked List
    fun reverseList(head: ListNode?): ListNode?{

        var current = head
        var previous : ListNode? = null
        var aux : ListNode? = null

        while (current != null){

            aux = current.next // save pointer to the next
            current.next = previous // pointer to previous Node
            previous = current // previous Node will be the current
            current = aux // current will be the pointer saved
        }

        return previous

    }

}

class ListNode(var value : Int){
    var next : ListNode? = null
}


fun main(){

    val solution = LinkedList()
    var Head = ListNode(1)
    var Node1 = ListNode(2)
    var Node2 = ListNode(3)
    var Node3 = ListNode(4)
    var Node4 = ListNode(5)

    Head.next = Node1
    Node1.next = Node2
    Node2.next = Node3
    Node3.next = Node4
    Node4.next = null

    solution.printList(solution.reverseList(Head))

}
