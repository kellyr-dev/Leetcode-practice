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

    // 383. Ransom Note
    fun canConstruct(ransomNote: String, magazine: String): Boolean {

        var hashOfransom = HashMap<Char, Int>()

        for (i in 0.. ransomNote.length-1){
            if (hashOfransom.containsKey(ransomNote.get(i))){
                var value = hashOfransom.get(ransomNote.get(i))
                hashOfransom.replace(ransomNote.get(i), value!!+1)
            }else{
                hashOfransom.put(ransomNote.get(i), 1)
            }
        }
        println(hashOfransom)

        for (i in 0.. magazine.length-1){

            if (hashOfransom.getOrElse(magazine.get(i)) {0} > 0 ){
                var valor = hashOfransom.get(magazine.get(i))
                hashOfransom.replace(magazine.get(i), valor!!-1)
            }
        }

        var values = hashOfransom.values.sum()
        println(hashOfransom.values)
        if (values > 0){
            return false
        }

        return true
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

    val value = TestClass.canConstruct("hello", "hellworld")
    println("result: ${value}")

}
