package Design

import kotlin.properties.Delegates
import kotlin.random.Random


class Station(

    var stationName: String,
    var tiempo: Int

) {

}

/*class Stations(

    var startStation : String,
    var endStation: String

){

}*/

class UndergroundSystem() {

    private var inputs : HashMap<Int, Station> = HashMap<Int, Station>()
    private var outputs : HashMap<Int, Station> = HashMap<Int, Station>()
    private var averageTime : HashMap<String, ArrayList<Int>> = HashMap<String, ArrayList<Int>>()
    // for each id in the Hashmap
    // I need store -> (stationName, t)
    // or use two HashMap one for Inputs (stationName, t)
    // other for Outputs (stationName t)
    // for each store it could be a array of

    // Sounds like I need three HashMap
    // 1 for inputs id
    // 2 for outputs id once id checked insert (startStation, endStation) and time in a third HashMap
    // 3 As I said before it will be used to store a list of time in order to calculate average of times


    fun checkIn(id: Int, stationName: String, t: Int) {

        if (inputs.containsKey(id)){
            println("This id is already registered in other station")
        }else{

            var aux = Station(stationName, t)
            inputs.put(id, aux)
        }

    }

    fun checkOut(id: Int, stationName: String, t: Int) {

        if (inputs.containsKey(id)){
            var endStation = Station(stationName, t)
            var startStation = inputs.get(id)

            var auxString = ""+startStation!!.stationName+","+stationName
            //println("auxString: ${auxString}")

            var timeToStorage = t - startStation.tiempo

            if (averageTime.containsKey(auxString)){
                println("Yes it contains: ${auxString}")
                var array = averageTime.get(auxString)
                array?.add(timeToStorage)
                averageTime.put(auxString, array!!)
                inputs.remove(id)

            }else {

                var array = ArrayList<Int>()
                array.add(timeToStorage)
                averageTime.put(auxString, array)
                inputs.remove(id)

            }

        }else{

            println("This id:${id} can't be checked because does not have a registered starStation")
        }

    }

    fun getAverageTime(startStation: String, endStation: String): Double {

        // var auxString = ""+startStation!!.stationName+","+stationName
        var startEndStation = ""+startStation+","+endStation
        //var startEndStation = Stations(startStation, endStation)
        if (averageTime.containsKey(startEndStation)){

            var arraOfTimes = averageTime.get(startEndStation)
            var qty : Double = 0.0

            if (arraOfTimes!!.size == 1){
                return arraOfTimes.get(0)/1.0
            }else{
                var suma = 0
                for (i in 0 .. arraOfTimes!!.size-1){
                    suma = suma + arraOfTimes[i]
                    qty += 1
                }
                return (suma/qty)
            }
        }else {

            println("Average time is empty does not exist record in time for this stations")
            return -1.0
        }

    }

    fun printAllAverageTime(){

        for (any in averageTime){
            println("(${any}) => ${any.value}")
        }
    }

}

fun main(){

    var system = UndergroundSystem()

    /*var listStartStation = listOf(

        "Carapita",
        "Capitolio",
        "Zona Rental",
        "Plaza Venezuela",
        "Sabana Grande",
        "Chacaito",
        "Chacao",
        "El Silencio",
        "Altamira",
        "Parque del Este",
        "Palo Grande",
        "Petare"
    )

    var listEndStation = listOf(

        "Carapita",
        "Capitolio",
        "Zona Rental",
        "Plaza Venezuela",
        "Sabana Grande",
        "Chacaito",
        "Chacao",
        "El Silencio",
        "Altamira",
        "Parque del Este",
        "Palo Grande",
        "Petare"
    )*/

    // 10 + 12 = 22/2 = 11.0

    var auxIn1 = Station("Leyton", 3) // 15-3 = 12/1
    var auxOut1 = Station("Waterloo", 15)

    var auxInt3 = Station("Leyton", 10) // 20 - 10 = 10
    var auxOut2 = Station("Waterloo", 20)

    var auxIn2 = Station("Paradise", 8) // 22 - 8 = 14
    var auxOut3 = Station("Cambridge", 22)

    // system.checkIn(10, "Leyton", 24) // 38 - 24 = 14 |
    // system.checkOut(10, "Waterloo", 38)
    //var aux44 = Station(listStartStation.get(Random.nextInt(0, 11)), 7)

    system.checkIn(45, auxIn1.stationName, auxIn1.tiempo)
    system.checkIn(32, auxIn2.stationName, auxIn2.tiempo)
    system.checkIn(27, auxInt3.stationName, auxInt3.tiempo)

    system.checkOut(27, auxOut2.stationName, auxOut2.tiempo)
    system.checkOut(32, auxOut3.stationName, auxOut3.tiempo)
    system.checkOut(45, auxOut1.stationName, auxOut1.tiempo)


    system.printAllAverageTime()
    println("Average: ${system.getAverageTime("Paradise", "Cambridge")}")
    system.printAllAverageTime()
    println("Average: ${system.getAverageTime("Leyton", "Waterloo")}")
    system.checkIn(10, "Leyton", 24)
    system.printAllAverageTime()
    println("Average: ${system.getAverageTime("Leyton", "Waterloo")}")
    system.checkOut(10, "Waterloo", 38)
    system.printAllAverageTime()
    println("Average: ${system.getAverageTime("Leyton", "Waterloo")}")
    //system.printAllAverageTime()


    /* case use

    ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime",

    "checkIn","getAverageTime","checkOut","getAverageTime"]

    [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10], [45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22], ["Paradise","Cambridge"],["Leyton","Waterloo"],

    [10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
     */


}