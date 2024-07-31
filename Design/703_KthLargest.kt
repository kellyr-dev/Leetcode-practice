package Design

import java.util.*
import kotlin.collections.ArrayList

// 703. Kth Largest Element in a Stream

class KthLargest(k:Int, nums: IntArray) {

    val pq: PriorityQueue<Int> = PriorityQueue<Int>()
    val kth = k

    init {
        for (num in nums){
            pq.add(num)
        }
    }

    fun add(value : Int): Int {
        pq.add(value)
        while (pq.size > kth){
            pq.poll()
        }
        return pq.peek()

    }
}

fun main(){

    val arrayInts = intArrayOf(4, 5, 8, 2)
    val ClassTest = KthLargest(3, arrayInts)
    println("Add:(${3})  ==> result: [${ClassTest.add(3)}]")
    println("Add:(${5})  ==> result: [${ClassTest.add(5)}]")
    println("Add:(${10})  ==> result: [${ClassTest.add(10)}]")
    println("Add:(${9})  ==> result: [${ClassTest.add(9)}]")
    println("Add:(${4})  ==> result: [${ClassTest.add(4)}]")

}