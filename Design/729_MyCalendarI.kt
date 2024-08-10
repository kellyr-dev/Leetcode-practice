package Design

import java.util.PriorityQueue

class MyCalendar(){

    private var pq = ArrayList<Pair<Int, Int>>()

    fun book(start: Int, end: Int): Boolean {

        if (pq.size > 0) {
            for (pair in pq){
                if (start < pair.second){
                    return false
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
    println("booking: ${calendar.book(10, 20)}")
    println("booking: ${calendar.book(15, 25)}")
    println("booking: ${calendar.book(20, 30)}")

 /*

["MyCalendar",
"book", [47,50] -> true if (start < list.end){
"book", [33,41] -> true     if (start < list.start) and (end < list.start) => return true
"book", [39,45] -> false 
"book", [33,42] -> false
"book", [25,32] -> true
"book", [26,35] -> false
"book", [19,25] -> true
"book", [3,8] -> true
"book", [8,13] -> true
"book", [18,27] -> false

Output:
[null,true,false,false,false,false,false,false,false,false,false]


  */

}