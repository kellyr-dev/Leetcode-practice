# 643. Maximum Average Subarray I
def findMaxAverage(nums, k):
    if k == 1:
        return float(max(nums))

    if len(nums) == 0:
        return 0

    if k >= len(nums):
        return float(sum(nums) / k)

    right = k - 1  # k = 3 || 7 || 2 .. etc
    max_avg = float()
    left = 0
    while right <= len(nums) - 1:
        # print(f"nums[left:right] -> {nums[left:right+1]}")
        avg = float(sum(nums[left:right + 1]) / k)
        if avg >= max_avg:
            max_avg = avg

        right += 1
        left += 1

    # print(max_avg)
    return max_avg

# 128. Longest Consecutive Sequence
def longestConsecutiveSequence(nums):
    # ELEGANT SOLUTION
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
        while left + 1 in values:
            cont += 1
            left += 1
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

    while right <= len(nums) - 1:

        suma = suma + nums[right]

        while suma >= target and left <= right:
            if (right - left + 1) <= min_len:
                min_len = right - left + 1

            suma = suma - nums[left]
            left += 1

        right += 1

    if (min_len != float('inf')):
        return min_len
    else:
        return 0

# 3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    hashmap = {}
    left = 0
    right = 0
    max_qty = float('-inf')

    # base cases
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1

    # move right pointer until end of array
    while right <= len(s) - 1:

        if s[right] not in hashmap:
            hashmap[s[right]] = right

        else:
            if len(hashmap) > max_qty:
                max_qty = len(hashmap)

            # if get a repeated character move left pointer until find
            # when move remove from hashmap
            while s[left] != s[right]:
                hashmap.pop(s[left])
                left += 1

            hashmap.pop((s[left]))
            hashmap[s[right]] = right
            # update pointer left to the start point of the new possible longest substring
            left += 1

        right += 1

    # if not repeat character max longest substring is len(hashmap)
    return max(max_qty, len(hashmap))

# 424. Longest Repeating Character Replacement
def characterReplacement(s, k):
    right = 0
    left = 0
    local_max = 0
    global_max = float('-inf')
    aux = k
    hashmap = {}

    while right <= len(s)-1:

        hashmap[s[right]] = 1 + hashmap.get(s[right], 0)

        while (right -left + 1) - max(hashmap.values()) > k:
            hashmap[s[left]] -= 1
            left += 1

        global_max = max(global_max, right - left + 1)
        right += 1

    return global_max

# 125. Valid Palindrome
def isPalindrome(s):
    aux = ""
    for i in range(len(s)):
        if s[i].isalnum():
            aux = aux + s[i].lower()

    right = len(aux) - 1
    left = 0

    if len(aux) <= 1:
        return True

    while left < right:
        if aux[left] != aux[right]:
            return False

        left += 1
        right -= 1

    return True

# 1031. Maximum Sum of Two Non-Overlapping Subarrays
def maxConsecutiveSubArrayKOverlaping(nums, firstLen, secondLen):

    # Time Complexity - > 4 call to maxConsecutiK function -> 4*O(n)
    # Space Complexity - > 4 arrays nums - > 4*O(n)

    array2opt = []
    for i in range(len(nums)):
        array2opt.append(nums[i])

    def maxConsecutiveK(array, k):

        sumsofar = sum(array[0:k])
        maxsum1 = sumsofar
        right = k
        left = 0
        leftIdx = left
        rightIdx = right - 1
        while right < len(array):

            sumsofar = sumsofar + array[right] - array[left]
            if sumsofar > maxsum1:
                maxsum1 = sumsofar
                leftIdx = left + 1
                rightIdx = right

            left += 1
            right += 1

        for i in range(len(array)):

            if i >= leftIdx and i <= rightIdx:
                array[i] = -1

        return maxsum1

    sum1_1 = maxConsecutiveK(nums, firstLen)
    sum2_1 = maxConsecutiveK(array2opt, secondLen)

    nums2 = []
    for i in range(len(nums)):
        if nums[i] != -1:
            nums2.append(nums[i])

    array2opt2 = []
    for i in range(len(array2opt)):
        if array2opt[i] != -1:
            array2opt2.append(array2opt[i])

    sum1_2 = maxConsecutiveK(nums2, secondLen)
    sum2_2 = maxConsecutiveK(array2opt2, firstLen)

    return max(sum1_1 + sum1_2, sum2_1 + sum2_2)

# 1100
def findKlenghtSubtringsWithNoRepeatChar(word, k):
    '''
        word = "havefunonleetcode", k = 5 -> 6
        word = "home", k = 5 -> 0

    '''

    if k > len(word):
        return 0

    right = k
    left = 0
    count_B = True
    count = 0
    map = {}
    result = []
    while right <= len(word): # O(n)

        for i in range(left, right): # O(k)
            if word[i] in map:
                map[word[i]] = map[word[i]] + 1

            else:
                map[word[i]] = 1

        print(map)
        for value in map.keys(): # O(k)
            if map[value] > 1:
                count_B = False

        if count_B:
            count += 1
            result.append("".join(map.keys()))

        map.clear() # O(k)
        count_B = True
        print(result)
        print("<======================>")
        right += 1
        left += 1

    return count


if __name__ == '__main__':
    nums = [8,20,6,2,20,17,6,3,20,8,12] # 15,14,12,
    target = 11
    k = 2
    s = "AAAB"
    firstLen = 5
    secondLen = 4
    word = "havefunonleetcode"
    k = 5

    print(findKlenghtSubtringsWithNoRepeatChar(word, k))
