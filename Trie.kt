
class TrieNode(){

    var children : ArrayList<TrieNode?>
    var isEndOfWord : Boolean = false

    init {
        children = ArrayList<TrieNode?>(26)
        for (i in 0..<children.size-1){
            children[i] = null
        }
    }
}

class Trie {

    private val root = TrieNode()

    fun insert(word: String){
        var aux : TrieNode = root

        for (i in 0..word.length-1){
            var index = word.get(i).code
            println("index: ${index}")

            if (aux.children[index] == null){
                aux.children[index] = TrieNode()
            }
            aux = aux.children[index]!!
        }
        aux.isEndOfWord = true
    }
    fun search(word: String) : Boolean{
        var aux : TrieNode = root
        for (i in 0..word.length-1){
            var index = word.get(i).digitToInt()
            if (aux.children[index] == null){
                return false
            }
            aux = aux.children[index]!!
        }
        return aux.isEndOfWord
    }


}