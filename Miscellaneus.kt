class Miscellaneus {

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

        return 0
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

    print(TestClass.findLongestChain(pairs))
}
