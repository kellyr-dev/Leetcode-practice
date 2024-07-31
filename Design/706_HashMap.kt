package Design

class MyHashMap() {

    private var key : Int = 0
    private val arrayI = IntArray(1000001)

    init {
        for (i in 0.. arrayI.size-1){
            arrayI[i] = -1
        }
    }

    fun put(key: Int, value: Int){
        arrayI.set(key, value)
    }

    fun get(key: Int): Int{
        return arrayI.get(key)
    }

    fun printingArray(){

        for (num in arrayI){
            print(""+num+" ")
        }
    }

}

fun main (){

    val ClassTest = MyHashMap()
    ClassTest.put(1000000, 1)
    println("Value in index:${1000000} ==> ${ClassTest.get(1000000)}")
    ClassTest.put(0, 2)
    println("Value in index:${0} ==> ${ClassTest.get(0)}")

    /*
        ["MyHashMap","put","get","put","get"]
        [[],[1000000,1],[1000000],[0,2],[0]]

     */
}