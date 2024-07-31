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

    // 1004. Max Consecutive Ones III
    fun longestOnes(nums: IntArray, k: Int): Int {

        var right = 0
        var left = 0
        var maxCount = 0
        var hashmap = 0

        while (right < nums.size){
            if (nums[right] == 0){
                if (hashmap < k){
                    hashmap += 1
                    maxCount = Math.max(maxCount, right - left)

                }else{
                    maxCount = Math.max(maxCount, right - left)
                    while (hashmap >= k){
                        if (nums[left] == 0){
                            hashmap -= 1
                            left += 1
                        }else{
                            left += 1
                        }
                    }
                    hashmap += 1
                }
            }else{
                maxCount = Math.max(maxCount, right - left)
            }
            right += 1
        }

        return Math.max(maxCount, right - left)
    }


}

fun main(args : Array<String>){

    val testClass = SlidingWindows()
    val testString = "pwwkew"
    val testInput = intArrayOf(0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1)
    println(testClass.longestOnes(testInput, 3))

}