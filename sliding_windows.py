from collections import defaultdict

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

    while right <= len(s) - 1:

        hashmap[s[right]] = 1 + hashmap.get(s[right], 0)

        while (right - left + 1) - max(hashmap.values()) > k:
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

# 1100. Find K length Substrings With No Repeated
def findKlenghtSubtringsWithNoRepeatChar(word, k):
    if k > len(word):
        return 0

    right = k
    left = 0
    count_B = True
    count = 0
    map = {}
    result = []
    while right <= len(word):  # O(n)

        for i in range(left, right):  # O(k)
            if word[i] in map:
                map[word[i]] = map[word[i]] + 1

            else:
                map[word[i]] = 1

        print(map)
        for value in map.keys():  # O(k)
            if map[value] > 1:
                count_B = False

        if count_B:
            count += 1
            result.append("".join(map.keys()))

        map.clear()  # O(k)
        count_B = True
        print(result)
        print("<======================>")
        right += 1
        left += 1

    return count

# 340 Longest Substring with K Distinct Characters
def longestSubstringwithKDistinctChars(word, k):
    table = {}
    right = 0
    left = 0
    aux_k = k
    result = float('-inf')

    print(word)
    while right < len(word):
        print(table)
        print(f"current: ", word[right])
        if word[right] in table:
            table[word[right]] = table[word[right]] + 1
            result = max(result, sum(table.values()))

        else:
            print(len(table))
            if len(table) < k:
                table[word[right]] = 1
                result = max(result, sum(table.values()))
            else:
                result = max(result, sum(table.values()))
                while len(table) >= k:
                    print("here")
                    if table[word[left]] > 1:
                        print(f"reduce -1 to :", table[word[left]])
                        table[word[left]] -= 1
                    else:
                        print(f"pop: ", word[left])
                        table.pop(word[left])
                    left += 1
                table[word[right]] = 1

        right += 1

    return result

# 904. Fruit Into Baskets
def totalFruit(fruits):
    table = {}
    right = 0
    left = 0
    max_pick = 0
    K = 2

    while right < len(fruits):

        if fruits[right] in table:
            table[fruits[right]] += 1
            max_pick = max(max_pick, right - left)

        else:

            if len(table) < K:
                table[fruits[right]] = 1
                max_pick = max(max_pick, right - left)
            else:
                max_pick = max(max_pick, right - left)
                while len(table) >= K and left < right:

                    if table[fruits[left]] > 1:
                        table[fruits[left]] -= 1
                    else:
                        table.pop(fruits[left])

                    left += 1

                table[fruits[right]] = 1

        right += 1

    return max(max_pick, right - left)

# 1004. Max Consecutive Ones III
def longestOnes(nums, k):
    table = {0: 0}
    right = 0
    left = 0
    max_lenght = 0

    while right < len(nums):

        if nums[right] == 0:
            if table.get(0) < k:
                max_lenght = max(max_lenght, right - left)
                table[0] += 1

            else:
                max_lenght = max(max_lenght, right - left)
                while table.get(0) >= k:
                    if nums[left] == 0:
                        left += 1
                        table[0] -= 1
                    else:
                        left += 1

                table[0] += 1

        else:
            max_lenght = max(max_lenght, right - left)

        right += 1

    return max(max_lenght, right - left)

# 567. Permutation in String
def findPermutationAux(str1, pattern):
    if len(pattern) > len(str1):
        return False

    if len(str1) == 0:
        return False

    if len(pattern) == 0:
        return False

    right = len(pattern)
    left = 0
    aux_pattern = sorted(pattern)

    while right <= len(str1):
        aux = sorted(str1[left:right])
        if aux == aux_pattern:
            return True

        right += 1
        left += 1

    return False

# 438. Find All Anagrams in a String
def findAllAnagrams(str1, pattern):
    if len(pattern) > len(str1):
        return []

    right = len(pattern)
    left = 0
    aux_pattern = sorted(pattern)
    result = []

    while right <= len(str1):
        aux = sorted(str1[left:right])
        if aux == aux_pattern:
            result.append(left)

        right += 1
        left += 1

    return result

# 2461. Maximum Sum of Distinct Subarrays With Length K (not checked)
def maximumSubarraySum(nums, k):
    if k > len(nums):
        return 0

    table = {}
    left = 0
    right = k - 1
    maxSum = sum(nums[0:k])  # question if k is inclusive in Python
    for i in range(k):
        if nums[i] not in table:
            table[nums[i]] = 1
        else:
            table[nums[i]] = table[nums[i]] + 1
            maxSum = 0
    right += 1
    print(f"starting: ", table)
    while right < len(nums):

        print(f"[right]: ", right)
        print(f"[left]: ", left)
        if nums[right] not in table:
            table[nums[right]] = 1
            aux = maxSum - nums[left] + nums[right]
            maxSum = max(maxSum, aux)

            if table[nums[left]] > 1:
                table[nums[left]] = table[nums[left]] - 1
            else:
                table.pop(nums[left])
            right += 1
        else:

            table[nums[right]] = table[nums[right]] + 1
            if table[nums[left]] > 1:
                table[nums[left]] = table[nums[left]] - 1
            else:
                maxSum = max(sum(table.values()), maxSum)
                table.pop(nums[left])
            right += 1

        print(table)
        print("<================>")
    return maxSum

# 76. Minimum Window Substring (not checked)
def minWindow(s, t):
    table = {}

    if len(t) > len(s):
        return ""

    for i in range(len(t)):
        if t[i] in table:
            table[t[i]] += 1
        else:
            table[t[i]] = 1

    table_compare = {}
    right = 0
    left = 0
    min_windows = float('inf')
    result = (-1,-1)

    while right < len(s):  # going to thru complete string

        if s[right] in table:
            if s[right] in table_compare:
                table_compare[s[right]] += 1
            else:
                table_compare[s[right]] = 1

        sames = True
        while left <= right and len(table_compare) == len(table) and sames:

            print(f"{table_compare} -> {table}")

            if len(table_compare) == len(table): # O(n)
                for value in table:
                    print(f"value: {value} -> table[value]:{table[value]} - table_compare[value]:{table_compare[value]}")
                    if table[value] != table_compare[value]:
                        sames = False
                        continue

            if sames:
                if (right - left) < min_windows:
                    min_windows = (right - left)
                    result = (left, right)

                if s[left] in table:
                    if table_compare.get(s[left]) > 1:
                        table_compare[s[left]] -= 1
                    else:
                        table_compare.pop(s[left])
                left+=1

        right +=1

    return s[result[0]:result[1]+1]

# Amazon Interview (question 1)
def getMaxConsecutiveON(servers, k):

    right = 0
    left = 0
    maxlenght = 0
    aux = k

    while aux > 0 and left < len(servers):

        while right < len(servers):
            if servers[right] == 0:
                if aux > 0:
                    aux -= 1
                    while right < len(servers) and servers[right] == 0:
                        maxlenght = max(maxlenght, right - left + 1)
                        right +=1
                else:
                    break
            else:
                maxlenght = max(maxlenght, right - left + 1)
                right += 1

        aux = k
        left += 1
        right = left

    return maxlenght

# Amazon Interview (question 2)
def getRedundantSubstring(string, a, b):

    # V =[0,1]
    # C =[0 .. 5]
    # akljfs | a=-2, b=1 | a * V + b * C|
    # |a * V + b * C| => |-2*0 + 1*1| = L => 1 ===> 5
    # |a * V + b * C| => |-2*0 + 1*2| = L => 2 ===> 4
    # |a * V + b * C| => |-2*0 + 1*3| = L => 3 ===> 3
    # |a * V + b * C| => |-2*0 + 1*4| = L => 4 ===> 2
    # |a * V + b * C| => |-2*0 + 1*5| = L => 5 ===> 1

    #================================================
    # V = [0,2]
    # C = [0,4]
    # abbacc | a=-1, b=2 | a * V + b * C
    # |a * V + b * C| => |-1*1 + 2*2| = L => 3 ===> 4
    # |a * V + b * C| => |-1*2 + 2*4| = L => 6 ===> 1

    vowels = {
        'a' : 0,
        'e' : 0,
        'i' : 0,
        'o' : 0,
        'u' : 0
    }
    C = 0

    for i in range(len(string)):

        if string[i] in vowels:
            vowels[string[i]] += 1
        else:
            C += 1

    V = sum(vowels.values())

    # for each combination of C and V using a,b and formula I need to check how many substring are in the string that comply with these variables

    combinations = 0
    result = []
    for i in range(C+1):

        for j in range(V+1):
            #aux_c, aux_v, str_len
            aux_c = i
            aux_v = j
            str_len = a*j + b*i
            left = 0
            right = str_len
            while right < len(string):

                for k in range(left, right):
                    if string[k] in vowels:
                        aux_v -= 1
                    else:
                        aux_c -= 1

                if aux_v == 0 and aux_c == 0:
                    combinations += 1
                    result.append(string[left:right+1])

                right += 1
                left += 1
                aux_c = i
                aux_v = j

    print(result)
    return combinations

def getRedundantSub(string, a, b):

    table_hash = defaultdict(int)
    table_hash[0] = 1
    vowels = 0
    consont = 0
    result = 0

    maximo2 = 5511098820 * 2
    maximo = 1216131524 * 2
    print(f"maximo: {maximo}")
    print(f"maximo2: {maximo2}")

    for char in string:
        if char in 'aeiou':
            vowels += 1
        else:
            consont += 1

        leN = (a - 1)*vowels + (b-1)*consont
        result += table_hash[leN]
        table_hash[leN] += 1

    return result

if __name__ == '__main__':
    nums = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    target = 11
    s = "AAAB"
    firstLen = 5
    secondLen = 4
    word = "odicf"
    s1 = "aabdec" # s1 = "abababab" -> s2 = "baba" -> "abab"
    s2 = "abc"
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]

    servers = [1,1,1,0,1,0,1,0,1,1,0,0,1,1]
    k = 2
    words = "akljfs"
    a = -2
    b = 1

    print(getRedundantSub(words, a,b))
