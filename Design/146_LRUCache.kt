package Design

// Implementation using LinkedHashMap class
class LRUCache(capacity: Int) {

    private var count = 0
    private val cap = capacity
    private var cachelinkedHashMap = LinkedHashMap<Int, Int>()


    fun get(key: Int): Int {

        if (cachelinkedHashMap.containsKey(key)){
            var valueIn = cachelinkedHashMap.get(key)!!
            cachelinkedHashMap.remove(key)
            cachelinkedHashMap.put(key, valueIn)
            return cachelinkedHashMap.get(key)!!
        }else{
            return -1
        }
    }

    fun put(key: Int, value: Int) {

        if (cachelinkedHashMap.containsKey(key)){
            cachelinkedHashMap.remove(key)
            cachelinkedHashMap.put(key, value)

        }else{

            if (count < cap){
                cachelinkedHashMap.put(key, value)
                count++

            }else{

                var aux = cachelinkedHashMap.keys.iterator().next()
                cachelinkedHashMap.remove(aux)
                cachelinkedHashMap.put(key, value)

            }
        }
    }

    fun printAllKeyvalues() {
        for (values in cachelinkedHashMap) {
            println("key: ${values.key} -> (${values.value})")
        }
    }

}

fun main(){

    val lRUCache = LRUCache(2)
    lRUCache.put(1, 1) // cache is {1=1}
    lRUCache.put(2, 2) // cache is {1=1, 2=2}
    println(lRUCache.get(1)) // return 1
    lRUCache.printAllKeyvalues()

    lRUCache.put(3, 3) // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.printAllKeyvalues()

    println(lRUCache.get(2))
     // returns -1 (not found)
    lRUCache.put(4, 4) // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    println(lRUCache.get(1))
    println(lRUCache.get(3))
    println(lRUCache.get(4))
    // expected: [null,null,null,2,null,null,-1]
    // output: [null,null,null,1,null,null,-1]
}

