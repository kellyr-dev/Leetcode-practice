package Design

class CustomStack(
    maxSize: Int
) {

    private var size = maxSize
    private var cont = 0
    private var elements = Array(maxSize, { i -> -1 })

    fun push(x: Int) {

        if (cont <= size-1){
            elements[cont] = x
            cont += 1
        }else{
            println("Stack overflow cap: "+size)
        }

    }

    fun pop(): Int {

        if (cont > 0){
            var aux = elements[cont-1]
            elements[cont-1] = -1
            cont -= 1
            return aux
        }else{
            return -1
        }

    }

    fun increment(k: Int, `val`: Int) {

        if (k > cont){

            for (i in 0..cont-1){
                elements[i] = elements[i] + `val`
            }
        } else {
            for (i in 0..k-1){
                elements[i] = elements[i] + `val`
            }
        }

    }

    override fun toString(): String {
        print("(")
        for (i in 0..size-1){

            if (i == size -1){
                print("${elements[i]}")
            }else{
                print("${elements[i]}, ")
            }
        }
        println(")")
        return super.toString()
    }



}

fun main(){

    var array1 = CustomStack(10)
    var array2 = CustomStack(100)

    for (i in 0..9){
        array1.push(i*100)
    }

    for (i in 0..99){
        array2.push(i*10)
    }
    println("array1: ${array1}")
    println(array1.pop())
    println(array1.pop())
    println(array1.pop())
    println("array1: ${array1}")
    array1.push(21231)
    array1.push(Int.MAX_VALUE)
    array1.push(Int.MAX_VALUE)
    array1.push(800)
    println(array1.pop())
    println(array1.pop())
    println(array1.pop())
    println(array1.pop())

    println("array1: ${array1}")
    array1.increment(6,10)
    println("array1: ${array1}")
    array1.increment(3,100)
    println("array1: ${array1}")

    // println("array1: ${array2}")


}