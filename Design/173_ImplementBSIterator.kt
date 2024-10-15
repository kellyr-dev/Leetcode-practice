package Design

// 173. Binary Search Tree Iterator

class TreeNode(var value: Int){
    var left : TreeNode? = null
    var right : TreeNode? = null
}

class BinarySearchIterator(root: TreeNode?){

    var iterator : Int = -1
    var arraySearch : ArrayList<Int> = ArrayList<Int>()

    init {
        dfs(root)
        print(arraySearch)
    }

    private fun dfs(root : TreeNode?){
        if (root == null){
            return
        }
        dfs(root.left)
        arraySearch.add(root.value)
        dfs(root.right)
    }

    fun next(): Int{

        iterator += 1
        if (iterator <= arraySearch.size-1){
            return arraySearch[iterator]

        }else{
            return Int.MIN_VALUE
        }

    }

    fun hasNext(): Boolean {

        if (iterator < arraySearch.size-1){
            return true
        }
        return false
    }
}

fun main(){

    var tree = TreeNode(7)
    tree.left = TreeNode(3)
    tree.right = TreeNode(15)
    tree.left!!.left = null
    tree.left!!.right = null
    tree.right!!.left = TreeNode(9)
    tree.right!!.right = TreeNode(20)

    var BST = BinarySearchIterator(tree)
    println(BST.next())
    println(BST.hasNext())


}