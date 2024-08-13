package Design

import java.util.PriorityQueue

class MyCalendar(){

    private var pq = ArrayList<Pair<Int, Int>>()

    fun book(start: Int, end: Int): Boolean {

        if (pq.size > 0) {
            for (pair in pq){
                if (start < pair.second){
                    if (end > pair.first){
                        return false
                    }
                }
            }
            pq.add(Pair(start,end))
            return true

        }else {
            pq.add(Pair(start,end))
            return true
        }
    }
}

fun main(){

    var calendar = MyCalendar()
    println("booking: ${calendar.book(47, 50)}")
    println("booking: ${calendar.book(33, 41)}")
    println("booking: ${calendar.book(39, 45)}")
    println("booking: ${calendar.book(33, 42)}")
    println("booking: ${calendar.book(25, 32)}")
    println("booking: ${calendar.book(26, 35)}")
    println("booking: ${calendar.book(19, 25)}")
    println("booking: ${calendar.book(3, 8)}")
    println("booking: ${calendar.book(8, 13)}")
    println("booking: ${calendar.book(18, 27)}")

}