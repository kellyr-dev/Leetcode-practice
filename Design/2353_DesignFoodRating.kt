package Design


import java.util.Collections
import kotlin.collections.HashMap

class FoodRatings(

    foods: Array<String>,
    cuisines: Array<String>,
    ratings: IntArray
){

    private var mapFood = HashMap<String, Int>() // { "food" : index_of_ratings } -> to avoid loop thru array
    private var mapCuisine = HashMap<String, ArrayList<FoodRating>>()
    private val cuisiArray = cuisines
    data class FoodRating(var rate: Int, var food: String) : Comparable<FoodRating> {
        override fun compareTo(other: FoodRating): Int {
            return when {
                rate < other.rate -> -1
                rate > other.rate -> 1
                else -> {
                    other.food.compareTo(food)
                }
            }
        }
    }
    /*
        {
            "cuisine" : [(5,sushi), (4.7,ramen), (4.5,miso)] // not in order because ArrayList O(n)
        }
        with this hashtable, I will only loop thru specific cuisine to update ratings
        and if using PriorityQueue I will get the Maximun/mininmun in O(1)
        Change Rating = O(n)
        getHightRating = O(n)
    */

    init {

        for (i in 0.. ratings.size-1){

            if (!(mapFood.containsKey(foods[i]))){
                mapFood.put(foods[i], i)
            }

            var pairAux = FoodRating(ratings.get(i), foods.get(i))

            if (mapCuisine.containsKey(cuisines.get(i))){
                var arraList = mapCuisine.get(cuisines.get(i)) // return an arrayList of Pair<Int, String>
                arraList!!.add(pairAux)
                mapCuisine.replace(cuisines.get(i), arraList) // check this one

            }else{

                var arraList = ArrayList<FoodRating>()
                arraList.add(pairAux)
                mapCuisine.put(cuisines.get(i), arraList)

            }
        }
    }

    fun changeRating(food: String, newRating: Int) {

        if (mapFood.contains(food)){
            var index = mapFood.get(food)
            var cuisineIndex = cuisiArray[index!!]

            var arrayFoodsInCuisines = mapCuisine.get(cuisineIndex)!!

            for (j in 0.. arrayFoodsInCuisines.size-1){

                if (arrayFoodsInCuisines[j].food == food){
                    arrayFoodsInCuisines[j].rate = newRating
                }
            }

        }else{
            println("It was not possible find that specific food")
        }

    }

    fun highestRated(cuisine: String): String {

        if (mapCuisine.containsKey(cuisine)){
            var maxRatingFood = mapCuisine.get(cuisine)
            var result = maxRatingFood!!.sortedDescending()

            println(result)
            return result.get(0).food

        }else{
            println("This kind of cuisine is not registered")
            return ""
        }

    }

    fun printCuisines(){
        for (cuisi in mapCuisine){
            println(cuisi)
        }
    }

    fun printAllFoodsAndRating(){

        for (food in mapFood) {
            println("for food:${food.key} -> ${food.value} ")
        }
    }

}

fun main(){


    var foods = arrayOf("cpctxzh", "bryvgjqmj", "wedqhqrmyc", "ee", "lafzximxh", "lojzxfel", "flhs")
    var cuisines = arrayOf("wbhdgqphq", "wbhdgqphq", "mxxajogm", "wbhdgqphq", "wbhdgqphq", "mxxajogm", "mxxajogm")
    var ratings = intArrayOf(15, 5, 7, 16, 16, 10, 13)
    var DesignSystem = FoodRatings(foods, cuisines, ratings)

    DesignSystem.printCuisines()

    DesignSystem.changeRating("lojzxfel", 1)
    println(DesignSystem.highestRated("mxxajogm"))
    println(DesignSystem.highestRated("wbhdgqphq"))
    println(DesignSystem.highestRated("mxxajogm"))

}