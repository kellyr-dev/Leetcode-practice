
# 643. Maximum Average Subarray I
def findMaxAverage(nums, k):

    if k == 1:
        return float(max(nums))

    if len(nums) == 0:
        return 0

    if k >= len(nums):
        return float(sum(nums)/k)

    right = k-1  # k = 3 || 7 || 2 .. etc
    max_avg = float()
    left = 0
    while right <= len(nums) - 1:
        #print(f"nums[left:right] -> {nums[left:right+1]}")
        avg = float(sum(nums[left:right+1]) / k)
        if avg >= max_avg:
            max_avg = avg

        right += 1
        left += 1

    # print(max_avg)
    return max_avg

# 128. Longest Consecutive Sequence
def longestConsecutiveSequence(nums):


    # ELEGANT SOLUTION
    '''
    uniques = set(nums)
        max_length = 0

        while uniques:
            low = high = uniques.pop()

            while low - 1 in uniques or high + 1 in uniques:
                if low - 1 in uniques:
                    uniques.remove(low - 1)
                    low -= 1

                if high + 1 in uniques:
                    uniques.remove(high + 1)
                    high += 1

            max_length = max(high - low + 1, max_length)

        return max_length

    '''
    values = {}
    for j in range(len(nums)):
        if nums[j] in values:
            values[nums[j]] = 1
        else:
            values[nums[j]] = 1

    max_consecutive = 1
    cont = 1
    for i in range(len(nums)):
        left = nums[i]
        print(f"left: ", left)
        while left+1 in values:
            cont += 1
            left +=1
            print(f"new left: {left}")

        print(f"cont: {cont}")
        if cont >= max_consecutive:
            max_consecutive = cont
        cont = 1

    return max_consecutive

# 209. Minimum Size Subarray Sum
def minimunSizeSubarraySum(nums, target):

    # base cases
    if (len(nums)) == 0:
        return 0
    if len(nums) == 1:
        if target >= nums[0]:
            return 0
        elif target < nums[0]:
            return 1

    right = 0
    left = 0
    min_len = float('inf')
    suma = 0

    while right <= len(nums)-1:

        suma = suma + nums[right]

        while suma >= target and left <= right:
            print(f"right: {right}")
            print(f"left: {left}")
            print(f"nums[left:right+1]", suma)
            print(f"______________________________")
            if (right - left + 1) <= min_len:
                min_len = right - left + 1

            suma = suma - nums[left]
            left += 1

        right += 1

    if (min_len != float('inf')):
        return min_len
    else:
        return 0


if __name__ == '__main__':

    nums = [1,2,3,4,5] # 15,14,12,
    k = 3
    target = 11

    print(minimunSizeSubarraySum(nums, target))