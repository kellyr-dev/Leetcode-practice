package Design

class Solution(nums: IntArray) {

    val original = IntArray(nums.size)
    val shuttle = nums
    init {
        for (i in 0 .. original.size-1){
            original[i] = nums[i]
        }
    }

    fun reset(): IntArray {
        return original
    }

    fun shuffle(): IntArray {

        var aux = shuttle
        var result = IntArray(shuttle.size)

        aux.shuffle()
        println("value: ${aux.size}")
        for (i in 0 .. aux.size-1){
            result[i] = aux[i]
        }
        return result
    }

}

fun main(){

    val Obje = Solution(intArrayOf(1,2,3))
    println(Obje.reset())
    println(Obje.shuffle())

}