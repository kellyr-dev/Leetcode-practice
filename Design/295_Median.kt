package Design

// 295. Find Median from Data Stream
class Median {

    var streamList = ArrayList<Int>()

    fun addNum(num: Int) {
        streamList.add(num)
    }

    fun findMedian(): Double {

        var tam = streamList.size
        var median = 0.0
        streamList.sort()

        if (tam % 2 == 0){
            var index1 = tam/2
            var index2 = index1 - 1
            median = (streamList.get(index1) + streamList.get(index2))/2.toDouble()

        }else{
            var index = (tam/2).toInt()
            median = streamList.get(index).toDouble()
        }
        return median
    }
}

fun main(){

    val aux = Median()
    aux.addNum(1)
    aux.addNum(2)
    println("Median: ${aux.findMedian()}")
    aux.addNum(3)
    println("Median: ${aux.findMedian()}")
}