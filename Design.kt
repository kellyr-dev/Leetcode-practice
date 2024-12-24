import java.util.*

// 155. Min Stack
class MinStack(){

    private var minStack = Stack<Int>()
    private var mainStack = Stack<Int>()

    fun push(value : Int){

        mainStack.push(value)
        if (minStack.empty() || value <= minStack.peek()){
            minStack.push(value)
        }
    }

    fun pop(){
        if (mainStack.peek().equals(minStack.peek())){
            minStack.pop()
        }
        mainStack.pop()
    }

    fun top(): Int{
        return mainStack.peek()
    }

    fun getMin():Int{
        return minStack.peek()
    }
}

// 295. Find Median from Data Stream
class MedianFinder(){
    
}

fun main(){

    val objeto = MinStack()
    objeto.push(-2)
    objeto.push(0)
    objeto.push(-3)
    println("getMin: "+ objeto.getMin())
    objeto.pop()
    println("top: "+objeto.top())
    println("getMin: "+ objeto.getMin())

}