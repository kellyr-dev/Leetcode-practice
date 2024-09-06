
def orderBSearch(nums, key):

    true = False # True -> ascending order | False -> Descending order
    if nums[0] > nums[len(nums)-1]:
        true = False
    else:
        true = True

    def helper(nums, key, left, right):

        middle = int((left + right)/2)

        if key == nums[middle]:
            return middle

        if middle < left or middle > right:
            return -1

        if true:
            if key > nums[middle]:
                return helper(nums, key, middle+1, right)
            else:
                return helper(nums, key, left, middle-1)
        else:
            if key > nums[middle]:
                return helper(nums, key, left, middle-1)
            else:
                return helper(nums, key, middle+1, right)

    result = helper(nums, key, 0, len(nums)-1)
    return result

# 35. Search Insert Position
def searchInsert(nums, target):

    left = 0
    right = len(nums)-1
    bestIndex = -1
    minDif = float('inf')

    while left <= right:
        middle = int((right + left)/2)

        if nums[middle] == target:
            return middle

        if target > nums[middle]:
            if abs(target - nums[middle]) <= minDif:
                minDif = min(abs(target - nums[middle]), minDif)
                bestIndex = middle + 1
            left = middle + 1
        else:
            right = middle - 1

    return bestIndex

# 35. Search Insert Position (Recursive)
def searchInsertRecursive(nums, target):

    if target < nums[0]:
        return 0
    if target > nums[len(nums)-1]:
        return len(nums)

    def helper(nums, target, left, right, bestIndex, minDif):
        middle = int((left + right)/2)

        if nums[middle] == target:
            return middle

        if left > right:
            return bestIndex

        if target > nums[middle]:
            if abs(target - nums[middle]) <= minDif:
                bestIndex = middle + 1
                minDif = abs(target - nums[middle])

            return helper(nums, target, middle+1, right, bestIndex, minDif)
        else:
            return helper(nums, target, left, middle-1, bestIndex, minDif)

    result = helper(nums, target, 0, len(nums)-1, -1, float('inf'))
    return result

# 744. Find Smallest Letter Greater Than Target
def nextGreatestLetter(letters, target):
    left = 0
    right = len(letters) - 1

    hash_table = {}

    for i in range(len(letters)):
        hash_table[letters[i]] = i

    print(hash_table)
    if target < letters[0]:
        return letters[0]

    if target > letters[len(letters) - 1]:
        return letters[0]

    if target in hash_table:
        index = hash_table[target]
        if index+1 <= len(letters)-1:
            return letters[index + 1]
        else:
            return letters[0]
    else:
        prev = hash_table[letters[0]]
        for value in hash_table.keys():
            if value > target:
                return value

            prev = value

# Minimum Difference Element
def searchMinDiffElement(arr, key):

    if key < arr[0]:
        return arr[0]
    if key > arr[len(arr)-1]:
        return arr[len(arr)-1]

    start = 0
    end = len(arr)-1
    minimunDiff = float('inf')
    result = -1

    while start <= end:
        middle = int((start + end)/2)
        print(f"minimunDiff: {minimunDiff}")
        if key < arr[middle]:
            if minimunDiff > (abs(key - arr[middle])):
                minimunDiff = abs(key - arr[middle])
                result = arr[middle]
            end = middle - 1
        elif key > arr[middle]:
            if minimunDiff > (abs(key - arr[middle])):
                minimunDiff = abs(key - arr[middle])
                result = arr[middle]
            start = middle + 1
        else:
            return arr[middle]

    return result

# 33. Search in Rotated Sorted Array
def rotateArray(arr, key):

    start = 0
    end = len(arr)-1

    while start < end:
        middle = int((start + end)/2)
        if arr[middle] == key:
            return middle
        if arr[middle] > arr[start]:
            start = middle
        else:
            end = middle

    indexMax = start
    start = 0
    newStart = indexMax + 1
    end = len(arr) - 1

    # here I have two ways to apply Binary Search
    # first way apply from start to indexMax
    # Second way apply from indexMax+1 to end

    if key >= arr[0] and key <= arr[indexMax]:
        result = binarySearchAux(key, arr, start, indexMax)
        if result is not None:
            return result

    if key >= arr[newStart] and key <= arr[end]:
        result = binarySearchAux(key, arr, newStart, end)
        if result is not None:
            return result

    return -1

def binarySearchAux(key, arr, start, end):

    while start <= end:
        middle = int((start + end)/2)
        if key == arr[middle]:
            return middle
        elif key > arr[middle]:
            start = middle+1
        else:
            end = middle-1

# 153. Find Minimum in Rotated Sorted Array
def findMin(nums):

    start = 0
    end = len(nums)-1

    while start < end:
        middle = int((start + end)/2)
        if middle < end and arr[middle] > arr[middle+1]:
            return middle + 1

        if middle > start and arr[middle-1] > arr[middle]:
            return middle

        if nums[start] < nums[middle]:
            start = middle + 1
        else:
            end = middle - 1

    return 0

if __name__ == '__main__':

    nums = [1,3,5,6]
    letters = ["e","e","e","k","q","q","q","v","v","y"]
    k = 10
    #arr = [4, 5, 6, 7, 0, 1, 2, 3]
    arr = [4, 5, 7, 9, 10, -1, 2]
    print(findMin(arr))
