import java.util.Collections

class Miscellaneus {

    var streamList = ArrayList<Int>()

    // 646. Maximum Length of Pair Chain
    fun findLongestChain(pairs: Array<Array<Int>>): Int {

        val pairSorted = pairs.sortedBy { it[1] }
        var maxCount = 1
        var i = 0
        var j = 1

        while (j < pairSorted.size){

            if (pairSorted[i][1] < pairSorted[j][0]){
                maxCount += 1
                i = j
            }
            j += 1
        }
        return maxCount
    }

    // 921. Minimum Add to Make Parentheses Valid
    fun minAddToMakeValid(s: String): Int {

        val stacks = ArrayDeque<Char>()
        var j = 0

        while (j < s.length){

            if (s[j] == '('){
                stacks.add(s[j])
            }else{
                if (stacks.size > 0){

                    if (stacks.last() == '(') {
                        stacks.removeLast()
                    }else{
                        stacks.add(s[j])
                    }

                } else{
                    stacks.add(s[j])
                }
            }
            j += 1

        }
        println("stacks: ${stacks}")
        return stacks.size
    }

}

fun main() {

    val TestClass = Miscellaneus()
    val pairs = arrayOf(
        arrayOf(7, 8),
        arrayOf(5, 6),
        arrayOf(1, 2),
        arrayOf(3, 5),
        arrayOf(4, 5),
        arrayOf(2, 3),
    )

    val value = TestClass.findLongestChain(pairs)
    println("result: ${value}")

}
