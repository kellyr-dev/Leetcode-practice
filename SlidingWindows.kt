class SlidingWindows {

    fun lengthOfLongestSubstring(s: String): Int {

        var left = 0
        var maxSubst = Int.MIN_VALUE
        val hashMap = HashMap<Char, Int>()

        for (right in 0 until s.length){

            if (!hashMap.containsKey(s.get(right))){
                hashMap.put(s[right], right)
            } else {

                if (hashMap.size >= maxSubst) {
                    maxSubst = hashMap.size
                }

                while (s[left] != s[right]){

                    hashMap.remove(s[left])
                    left++
                }
                hashMap.remove(s[left])
                hashMap.put(s[right], right)
                left++;

            }
        }
        return Math.max(hashMap.size, maxSubst)
    }
}

fun main(args : Array<String>){

    val testClass = SlidingWindows()
    val testString = "pwwkew"
    println(testClass.lengthOfLongestSubstring(testString))

}