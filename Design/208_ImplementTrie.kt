package Design

class Trie() {

    private var mapSearch = HashMap<String, Int>()
    private var mapSearchWith = HashMap<String, Int>()

    fun insert(word: String) {

        if ((!mapSearch.containsKey(word))){
            mapSearch.put(word, 1)


            var j = word.length-1
            while (j >= 0){
                var stringAux = word.slice(0..j)
                if (!(mapSearchWith.containsKey(stringAux))){
                    mapSearchWith.put(stringAux, 1)
                }
              //  println("prefix: ${stringAux}")
                j-= 1
            }
        }
    }

    fun search(word: String): Boolean {

        if (mapSearch.containsKey(word)){
            return true
        }else{
            return false
        }
    }

    fun startsWith(prefix: String): Boolean {

        if (mapSearchWith.containsKey(prefix)){
            return true
        }else{
            return false
        }

    }

}

fun main(){

    val trie = Trie()

    trie.insert("apple")
    println(trie.search("apple"))
    println(trie.search("app"));     // return False
    println(trie.startsWith("app")); // return True
    trie.insert("app");
    println(trie.search("app"));     // return True

}