

class BinarySearch{

    // 35. Search Insert Position
    fun searchInsert(nums: IntArray, target: Int): Int {

        var left = 0
        var right = nums.size-1
        var bestIndex = -1
        var minDiff = Int.MAX_VALUE
        var middle = 0

        if (target < nums[0]){
            return 0
        }

        if (target > nums[nums.size-1]){
            return nums.size
        }

        while (left <= right){

            middle = ((left + right)/2).toInt()

            if (target == nums[middle]){
                return middle
            }

            if (target > nums[middle]){
                left = middle + 1
                if (Math.abs(target - nums[middle]) <= minDiff){
                    minDiff = Math.abs(target - nums[middle])
                    bestIndex = middle + 1
                }

            }else{
                right = middle - 1
            }

        }
        return bestIndex
    }

    // 33. Search in Rotated Sorted Array
    fun searchRotate(nums: IntArray, target: Int): Int {

        if (nums.size == 1){
            if (nums[0] == target){
                return 0
            }else{
                return -1
            }
        }

        var start = 0
        var end = nums.size-1
        var middle = -1

        while (start < end){
            middle = ((start + end)/2).toInt()

            if (target == nums[middle]) {
                return middle
            }
            if (nums[start] < nums[middle]){
                start = middle
            }else{
                end = middle
            }
        }

        var maxIndex = start
        var newStart = maxIndex + 1
        start = 0
        end = nums.size-1
        var result: Int

        if (target >= nums[start] && target <= nums[maxIndex]){
            result = binarySearch(nums, target, start, maxIndex)
            if (result != -1){
                return result
            }
        }

        if (target >= nums[newStart] && target <= nums[end]){
            result = binarySearch(nums, target, newStart, end)
            if (result != -1){
                return result
            }
        }

        return -1
    }

    private fun binarySearch(nums: IntArray, target: Int, start: Int, end: Int) : Int {

        var middle: Int
        var indexStart = start
        var indexEnd = end
        while (indexStart <= indexEnd){
            middle = ((indexStart + indexEnd)/2).toInt()

            if (target == nums[middle]){
                return middle
            }else if (target > nums[middle]){
                indexStart = middle + 1
            }else{
                indexEnd = middle - 1
            }
        }
        return -1
    }

    // 153. Find Minimum in Rotated Sorted Array
    fun findMin(nums: IntArray): Int {

        return  -1
    }

}

fun main(){

    val aux = BinarySearch()
    //var nums = intArrayOf(4,5,6,7,0,1,2)
    var nums = intArrayOf(1)
    val key = 3
    println(aux.searchRotate(nums, key))

}