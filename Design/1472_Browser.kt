package Design

// 1472. Design Browser History (no checked)
class BrowserHistory(homepage: String) {

    private var stack = ArrayList<String>()
    private var index = 0
    var iterator = -1

    init {
        iterator += 1
        stack.add(index, homepage)
        index += 1
    }

    fun visit(url: String){

        iterator += 1
       // if (iterator > stack.size-1){
        stack.add(iterator, url)

        //stack.add(index, url)
        index += 1
    }

    fun back(steps: Int): String {

        var aux = iterator - steps

        if ((iterator - steps) < 0){
            iterator = 0
            return stack.get(0)
        }else{
            iterator = aux
            return stack.get(aux)
        }
    }

    fun forward(steps: Int): String{
        if ((iterator + steps) > stack.size-1){
            return stack.get(iterator)
        } else {
            iterator = iterator + steps
            return stack.get(iterator)
        }

    }

    fun printingAllUrl(){

        for (url in stack){
            print("${url} -> ")
        }
        print("it:[${iterator}]")
        println()
    }
}

fun main(){

    // Example 1
    /*val TestClase = BrowserHistory("esgriv.com")
    TestClase.visit("cgrt.com")
    TestClase.visit("tip.com")
    TestClase.printingAllUrl()
    println("back: "+TestClase.back(9))
    TestClase.visit("kttzxgh.com")
    TestClase.printingAllUrl()
    println("forward: "+TestClase.forward(7))
    TestClase.visit("crqje.com")
    TestClase.printingAllUrl()
    TestClase.visit("iybch.com")
    TestClase.printingAllUrl()
    println("forward: "+TestClase.forward(5))
    TestClase.visit("uun.com")
    TestClase.printingAllUrl()
    println("back: "+TestClase.back(10))
    TestClase.visit("hci.com")
    TestClase.printingAllUrl()
    TestClase.visit("whula.com")
    TestClase.printingAllUrl()
    println("forward: "+TestClase.forward(10))*/

    /*
    ["BrowserHistory", => ["esgriv.com"]    | null
    "visit", => ["cgrt.com"]                | null
    "visit", => ["tip.com"]                 | null
    "back", => [9]                          | "esgriv.com"
    "visit", => ["kttzxgh.com"]             | null
    "forward", => [7]                       | kttzxgh.com
    "visit", => ["crqje.com"]               | null
    "visit", => ["iybch.com"]               | null
    "forward", => [5]                       | "iybch.com"
    "visit", => ["uun.com"]                 | null
    "back", => [10]                         | "esgriv.com"
    "visit", => ["hci.com"]                 | null
    "visit", => ["whula.com"]               | null
    "forward" => [10]                       | "whula.com"
    */

    // Example 2
    val TestClase = BrowserHistory("leetcode.com")
    TestClase.visit("google.com")
    TestClase.visit("facebook.com")
    TestClase.visit("youtube.com")
    TestClase.printingAllUrl()
    println("back: "+TestClase.back(1))
    println("back: "+TestClase.back(1))
    println("forward: "+TestClase.forward(1))
    TestClase.visit("linkedin.com")
    TestClase.printingAllUrl()
    println("forward: "+TestClase.forward(2))
    println("back: "+TestClase.back(2))
    println("back: "+TestClase.back(7))
}