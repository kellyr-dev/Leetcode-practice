package Design

// Interview at SnapInc

class SnapInc (redValue: Int, greenValue: Int, blueValue: Int) {

    protected val R = redValue
        get() = field
    protected val G = greenValue
        get() = field
    protected val B = blueValue
        get() = field


    fun isValid(): Boolean{
        if ((R < 0 || R > 255) || (G < 0 || G > 255) || (B < 0 || B > 255)){
            return false;
        }
        return true;
    }

    companion object {
        fun generateGradient(a : SnapInc, b : SnapInc, k: Int): List<SnapInc>{

            if (!(a.isValid() && b.isValid())){
                println("Values RGB are invalid!")
                return ArrayList<SnapInc>()
            }

            val result = ArrayList<SnapInc>()
            result.add(a)

            var auxR = a.R - b.R //100 - 150 = 50
            var auxG = a.G - b.G
            var auxB = a.B - b.B

            var mulR = a.R/k
            var mulG = a.G/k
            var mulB = a.B/k

            if (mulR == 0){
                mulR = b.R/k
            }
            if (mulG == 0){
                mulG = b.G/k
            }
            if (mulB == 0){
                mulB = b.B/k
            }

            if (auxR > 0) {
                mulR = -mulR

            }else {
                if (auxR ==0){
                    mulR =0
                }
            }

            if (auxG > 0){
                mulG = -mulG
            }else {
                if (auxG == 0){
                    mulG = 0
                }
            }

            if (auxB > 0){
                mulB = -mulB
            }else {
                if (auxB == 0){
                    mulB = 0
                }
            }

            var factorR = 1
            var factorB = 1
            var factorG = 1

            for (i in 1..k){

                factorR = (mulR * i)
                factorG = (mulG * i)
                factorB = (mulB * i)

                var aux = SnapInc(a.R + factorR, a.G + factorG, a.B + factorB)
                result.add(aux)
            }
            return result
        }
    }

    override fun toString(): String {
        return "(${this.R}:${this.G}:${this.B})->"
    }
}

fun main(){

    val a = SnapInc(255,0,100)
    val b = SnapInc(255, 160, 0)
    val k = 5

    val results = SnapInc.generateGradient(a,b,k)

    for (RGB in results){
        print(RGB)
    }

}