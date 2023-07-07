from math import sqrt

# PRACTICE DINAMYC PROGRAMMING FOR CODING INTERVIEWS
# SOME PROBLEMS FROM LEETCODE

# Partition equal subset sum -> 0/1 Knapsack
# 416 leetcode
# 1) Backtracking / Recursion
# get sum, target will be sum/2
# check if impar number because no posible get sum/2 if impar number
# apply 0/1 Knapsack with variables above

def partition_equal_subset_sum(nums):

    dp = {}
    suma = sum(nums)
    target = int(suma/2)

    print(f"Sum: ",suma)
    print(f"target: ", target)
    print(f"ODD: ", suma%2)

    if suma % 2 == 0:
        def helper(nums, target, dp):

            if target in dp:
                return dp[target]

            if target == 0:
                return True

            if target < 0:
                return False

            if len(nums) == 0:
                return False

            value = helper(nums[1:], target, dp) or helper(nums[1:], target - nums[0], dp)
            dp[target] = value

            return value

        result = helper(nums, target, dp)
        return result
    else:
        return False

def count_of_subsets_with_given_sum(nums, target):

    def helper(nums, target):

        if target == 0:
            return 1

        if target < 0:
            return 0

        if len(nums) == 0:
            return 0

        value = helper(nums[1:], target) + helper(nums[1:], target - nums[0])
        return value

    result = helper(nums, target)
    print(f"result: ",result)
    return result

# find the number of ways since a diff given
# input: [3,1,2,3] and diff = 3
# 1way [3,1,2] - [3] = 3
# 2way [3,3] - [1,2] = 3
# s1 - s2 = diff (1)
# sum = s1 + s2 => s2 = sum - s1 (2)
# s1 - (sum - s1) = diff
# 2s1 = diff + sum
# s1 = (diff + sum)/2
# new problem is count num subtset with a sum given (already solved)

def count_num_subset_given_a_diff(nums, diff):

    suma = sum(nums)
    target = int((suma + diff)/2)
    dp = {}

    def helper(nums, target, index):

        key = (index, target)

        if key in dp:
            return dp[key]

        if index == len(nums):
            if target == 0:
                return 1
            else:
                return 0

        value = (helper(nums, target, index+1) + helper(nums, target - nums[index], index+1))
        dp[key] = value
        return value

    result = helper(nums, target, 0)
    return result


dp = {}
def target_sum(nums, target):

    # s1 + s2 = sum; => (s2 = sum - s1)
    # s1 = sum(-nums);
    # s2 = sum(nums);
    # s1 - s2 = target
    # s1 - (sum - s1) = target
    # s1 = (sum + targe)/2

    suma = sum(nums)
    new_target = int((suma + target)/2)

    def helper(nums, new_target, index):

        key = (index, new_target)
        if key in dp:
            return dp[key]

        if index == len(nums):
            if new_target == 0:
                return 1
            else:
                return 0

        value = helper(nums, new_target - nums[index], index+1) + helper(nums, new_target, index+1)
        dp[key] = value
        print(dp)
        return value

    result = helper(nums, new_target, 0)
    return result

def coin_change(coins, amount):

    dp = {}
    def helper(coins, amount, index):

        key = (index, amount)

        if key in dp:
            return dp[key]

        if amount == 0:
            return 0

        if amount < 0:
            return float('inf')

        if index == len(coins):
            return float('inf')

        value = min(1 + helper(coins, amount - coins[index], index), helper(coins, amount, index+1))
        dp[key] = value
        return value

    result = helper(coins, amount, 0)

    if result == float('inf'):
        return -1
    else:
        return result

def coin_changeII(coins, amount):
    dp = {}

    def helper(coins, amount, index):

        key = (index, amount)

        if key in dp:
            return dp[key]

        if amount == 0:
            return 1

        if amount < 0:
            return 0

        if index == len(coins):
            return 0

        value = helper(coins, amount - coins[index], index) + helper(coins, amount, index + 1)
        dp[key] = value
        return value

    result = helper(coins, amount, 0)
    return result

# O/1 Knapsack - Unbounded
def rod_cutting(length, profit, l):

    dp = {}
    def helper(length, profit, l, index):

        key = (index, l)

        if key in dp:
            return dp[key]

        if l == 0:
            return 0

        if l < 0:
            return 0

        if index == len(length):
            return 0

        if length[index] <= l:
            value = max(profit[index] + helper(length, profit, l - length[index], index), helper(length, profit, l, index+1))
            dp[key] = value
            return value
        else:
            value = helper(length, profit, l, index+1)
            dp[key] = value
            return value

    result = helper(length, profit, l, 0)
    return result

# 0/1 Knapsack bounded
# I had to choose a key that combine all varible in this case the two pointer (left, right) and my value W
# capacity W (in terms of Knapsack problem nomenclature)
# both pointer must not cross, so left < right must be a condition
# SOLVED but must be done by SLIDING WINDOWS approach
def reduceXto0(nums, X):

    right = len(nums)-1
    dp = {}

    print(f"nums", nums)
    print(f"right: ", len(nums)-1)

    def helper(nums, X, left, right):

        key = str(X)+","+str(left)+","+str(right)
        #print(key)

        if key in dp:
            print(dp)
        #    return dp[key]

        if X == 0:
            return 0

        if X < 0:
            return float('inf')

        if left >= len(nums):
            return float('inf')

        if right < 0:
            return float('inf')

        if left > right:
            return float('inf')

        value_left = 1+helper(nums, X - nums[left], left+1, right)
        value_right = 1+helper(nums, X - nums[right], left, right-1)
        value = min( value_left, value_right )

        dp[key] = value
        return value

    result = helper(nums, X, 0, right)
    if result == float('inf'):
        return -1
    else:
        return result
# 97 LeetCode
# Basically is try to find 5 using all letter from S1 and S2
# len(s1) + len(s2) == len(t)

def isInterleave(s1, s2, t):

    if len(s1) + len(s2) != len(t):
        return False

    def helper(s1, s2, t, index_s1, index_s2, index_t):

        if index_t == len(t):
            if index_s1 == len(s1) and index_s2 == len(s2):
                return True

            if index_s1 < len(s1) or index_s2 < len(s2):
                print("final of t3 but not in s1 or  S2")
                return False

        if index_s1 == len(s1):
            if s2[index_s2] == t[index_t]:
                helper(s1, s2, t, index_s1, index_s2 + 1, index_t + 1)
            else:
                return False

        if index_s2 == len(s2):
            if s1[index_s1] == t[index_t]:
                helper(s1, s2, t, index_s1 + 1, index_s2, index_t + 1)
            else:
                return False

        left = False
        right = False
        if s1[index_s1] == t[index_t]:
            left = helper(s1, s2, t, index_s1+1, index_s2, index_t+1)
        if s2[index_s2] == t[index_t]:
            right = helper(s1, s2, t, index_s1, index_s2+1, index_t+1)

        return left or right

    result = helper(s1, s2, t, 0, 0, 0)

    print(result)
    return result

# TOTALLY SAME EXCERCISE LIKE LONGEST COMMON SUBSEQUENCE
# find max lines without crossed
# is like to think knapsack bounded because the order matters (iteration into index array)
# O/1 knapsack if match lines I took but if not I have to pick separately in each recursion call and calculate max
# max(helper(index_i+1, index_j), helper(index_i, index_j+1))
# if match call helper(index_i+1, index_j+1)

def uncrosedlines(nums1 , nums2):

    #print(nums1)
    dp = {}
    def helper(nums1, nums2, i, j):

        if i == len(nums1) or j == len(nums2):
            return 0

        key = (i,j)

        if key in dp:
            return dp[key]

        if nums1[i] == nums2[j]:
            temp = 1 + helper(nums1, nums2, i+1, j+1)
            dp[key] = temp
            return temp
        else:
            temp = max(helper(nums1, nums2, i+1, j), helper(nums1, nums2, i, j+1))
            dp[key] = temp
            return temp

    result = helper(nums1, nums2, 0, 0)
    return result

# Longest repeating subsequence
# "AAAB"
# "AB"
# Output = 2 or True

def longest_repeating_subsquence(text1, text2):

    dp = {}
    longest_string = []
    def helper(text1, text2, i, j):

        if i == len(text1) or j == len(text2):
            return 0

        key = (i,j)

        if key in dp:
            return dp[key]

        if text1[i] == text2[j] and i != j:
            tmp = 1 + helper(text1, text2, i+1, j+1)
            longest_string.append(text1[i])
            dp[key] = tmp
            return tmp
        else:
            tmp = max(helper(text1, text2, i+1, j), helper(text1, text2, i, j+1))
            dp[key] = tmp
            return tmp

    result = helper(text1, text2, 0, 0)
    print(longest_string)
    return result

def patternMatching(text, patter):

    def helper(text, pattern, i, j):

        if j == len(pattern):
            return True

        if i == len(text):
            return False

        if text[i] == pattern[j]:
            return helper(text, pattern, i+1, j+1)
        else:
            return helper(text, pattern, i+1, j)

    result = helper(text, patter, 0, 0)
    return result

def longestIncreasingSubsequence(nums):

    # base case (if j == len(nums))
    #               return 0
    # i = 0, j= 1
    # [0,1,0,3,2,3] => i=0, j=1
    #  ^ ^       [0,1,0,3,2,3]
    #               /      \  => if nums[j] < nums[i]
    #  max(0,[1,0,3,2,3]    0,[1,3,2,3])
    #       /   \                   /  \
    #max(1,[3,2,3]  1,[2,3])
    #
    # if nums[j] > nums[i]
    #   j++, cont+1
    #   call 1 + function(j++)
    # else -> return 0 + function (i++, j++)
    #
    # INPUT:

    # if array[j] < array[i]
    #   cont+1, j++
    # else
    #
    # [10, 9, 2, 5, 3, 7, 101, 18]
    #  i^
    # [10, 9, 2, 5, 3, 7, 101, 18]

    dp = {}
    def helper(nums, i, j):

        if i == len(nums) or j == len(nums):
            return 0

        key = (i,j)

        if key in dp:
            return dp[key]

        if nums[j] > nums[i]:
            tmp = max(1 + helper(nums, i+1, j+1), helper(nums, i+1, j+1))
            dp[key] = tmp
            return tmp
        else:
            tmp = max(helper(nums, i+1, j+1), helper(nums, i+1, j+1))
            dp[key] = tmp
            return tmp

    result = helper(nums, 0, 1)
    print(dp)
    return result

# DP SOLUTION // NOT BACKTRACKING IS A GOOD APPROACH
def longesIncreasingSubsequenceDP(nums):

    LIS = [1] * len(nums)
    #print(LIS)

    # len(nums) = 4 => [2,4,3,7]
    for i in range(len(nums), -1, -1): # 4 to 0 (-1 index not include)
        for j in range(i + 1, len(nums)): # first is 4, after is 3 and 4, after is 2, 3 and 4
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    return max(LIS)

def RussianDollEnvelopes(envelopes):

    nueva = sorted(envelopes) # nlog(n) -> if using QuickSort/MergeSort/Heapsort

    LIS = [1] * len(nueva)
    maxValue = 1

    for i in range(len(nueva)-1, -1, -1):
        h = nueva[i][0]
        w = nueva[i][1]
        keyi = (h, w)
        print(keyi)
        for j in range(i+1, len(nueva)):
            hj = nueva[j][0]
            wj = nueva[j][1]
            if h < hj and w < wj:
                LIS[i] = max(LIS[i], 1+LIS[j])

            if maxValue < LIS[i]:
                maxValue = LIS[i]

    return maxValue


# KELLY APPROACH THRU BACKTRACKING -> GOOD but O(3^len(s1)+len(s2)) exponential time
# NEED TO CHECK DP APROACH
def editDistance(s1, s2):

    if len(s1) == 0:
        return len(s2)

    if len(s2) == 0:
        return len(s1)

    dp = {}
    def helper(s1, s2, i, j):

        if i == len(s1) and j == len(s2):
            return 0

        if i== len(s1) and j != len(s2):
            return len(s2)-j

        if i != len(s1) and j == len(s2):
            return len(s1)-i

        key = (i, j)

        if key in dp:
            return dp[key]

        if s1[i] == s2[j]:
            tmp = helper(s1, s2, i+1, j+1)
            dp[key] = tmp
            return tmp
        else:
            tmp = 1 + min(helper(s1, s2, i+1, j), helper(s1, s2, i, j+1), helper(s1, s2, i+1, j+1))
            dp[key] = tmp
            return tmp

    result = helper(s1, s2, 0, 0)
    return result

# THIS DP Approach a much better than BackTracking approach
def editDistanceDP(s1, s2):

    dp = [ [0] * (len(s2)+1) for _ in range(len(s1)+1)]

    for j in range(len(s2)+1):
        dp[0][j] = j

    for i in range(len(s1)+1):
        dp[i][0] = i

    print(dp)

    for i in range(len(s1)):
        for j in range(len(s2)):

            if j == len(s2):
                dp[i+1][j+1] = len(s1) - i
                continue

            if i == len(s1):
                dp[i + 1][j + 1] = len(s2) - j
                continue

            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i + 1][j + 1] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i][j])

    print(dp)
    print(dp[len(s1)][len(s2)])

# Maximun Sum circular Array (Kadence Algoritm)
def maximunSumCircular(nums):

    max_ending_here = 0
    max_so_far = float('-inf')
    sum_array = 0
    cont_nega = 0
    max_num = float('-inf')

    # Sum(Array) but check if all items are negative
    for j in range(len(nums)):
        sum_array += nums[j]

        if nums[j] < 0:
            cont_nega += 1
            if nums[j] > max_num:
                max_num = nums[j]

        nums[j] = nums[j] * -1

    # All num are negative return min num
    if cont_nega == len(nums):
        return max_num

    print(nums)

    # Kadence Algoritm with inversed array
    for i in range(len(nums)):

        max_ending_here += nums[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    max_so_far = max_so_far * -1
    print(f"sum_array: ", sum_array)
    print(f"max_so_far: ", max_so_far)

    return sum_array - max_so_far

# Backtracking LeetCode 62
def uniquePath(m, n):

    dp = {}
    def helper(m, n):

        if m == 0 or n == 0:
            return 0

        key = (m,n)

        if key in dp:
            return dp[key]

        if m == 1 and n == 1: # here el truco es validar con 1 # tambien en DP approach
            return 1
        else:
            tmp = helper(m-1, n) + helper(m, n-1)
            dp[key] = tmp
            return tmp

    result = helper(m, n)
    return result

# DP LeetCode 62
def uniquePathDP(m, n):

    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):

            if i== 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


# Backtracking APPROACH LeetCode 63
# num of path to reach m,n in the grid/matrix with obstacules
# obstacules are represented by 1
def uniquePathII(matrix):

    m = len(matrix)
    n = len(matrix[0])

    print(f"m: ",m)
    print(f"n: ",n)

    dp = {}
    def helper(m, n):

        if m <= 0 or n <= 0:
            return 0

        if matrix[m-1][n-1] == 1:
            return 0

        key = (m,n)

        if key in dp:
            return dp[key]

        if m == 1 and n == 1: # here el truco es validar con 1 # tambien en DP approach
            return 1
        else:
            tmp = helper(m-1, n) + helper(m, n-1)
            dp[key] = tmp
            return tmp

    result = helper(m, n)
    return result

# Backtracking APPROACH in a MATRIX LeetCode 64
# Minimun Path in a matrix moving only right and down until find m,n in the grid
def minimunPathSum(matrix):

    m = len(matrix)
    n = len(matrix[0])

    dp = {}
    def helper(m, n):

        if m <= 0 or n <= 0:
            return float('inf')

        key = (m, n)

        if key in dp:
            return dp[key]

        if m == 1 and n == 1:  # here el truco es validar con 1 # tambien en DP approach
            return matrix[m-1][n-1]
        else:
            tmp = matrix[m-1][n-1] + min(helper(m - 1, n), helper(m, n - 1))
            dp[key] = tmp
            return tmp

    result = helper(m, n)
    return result

def maximalSquareOf1s(matrix):

    dp = [ [0] * (len(matrix[0])+1) for _ in range(len(matrix)+1) ]

    print(matrix)
    print(dp)

    #print(dp)
    maxlengh = 0
    for i in range(1, len(matrix)+1):
        for j in range(1, len(matrix[0])+1):
            if matrix[i-1][j-1] == "1":
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                if dp[i][j] > maxlengh:
                    maxlengh = dp[i][j]

    print(dp)
    return maxlengh

# given a target string and a array of words write a function that return Boolean
# if combining elements in the array can construct the target.
memo = {}
def canConstruct(target, wordBank):

    if len(target) == 0:
        return True

    if target in memo:
        return memo[target]

    for words in wordBank:
        if target.startswith(words):
            suffix = target.replace(words, "")
            if canConstruct(suffix, wordBank) == True:
                memo[target] = True
                return True

    memo[target] = False
    return False

# count in how many ways we can Construct the target word given
# with the array of letter, words in wordBank
def countCanConstruct(target, wordBank):

    if target in memo:
        return memo[target]

    if len(target) == 0:
        return 1

    totalcount = 0
    for words in wordBank:

        if target.startswith(words):
            suffix = target.replace(words, "")

            eachcount = countCanConstruct(suffix, wordBank)
            totalcount = eachcount + totalcount

    memo[target] = totalcount
    return totalcount

# longest common substring (Different to Subsequence -> already solved)
def longestCommonSubstring(text1, text2):

    visited = {}
    string_sub = []

    def helper(i, j, conta):

        key = (i, j)

        if i >= len(text1) or j >= len(text2):
            return conta

        if key in visited:
            return visited[key]

        if text1[i] == text2[j]:
            conta = helper(i+1, j+1, conta+1)

        conta = max(conta, max(helper(i+1, j,0), helper(i, j+1,0) ))
        return conta

    result = helper(0,0, 0)
    print(result)

# DP APPROACH
def longestCommonSubstringDP(text1, text2):

    dp = [ [0]* (len(text2)+1) for _ in range(len(text1)+1) ]

    maxlength = float('-inf')

    for i in range(1, len(text1)+1 ):
        for j in range(1, len(text2)+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j] > maxlength:
                    maxlength = dp[i][j]
            else:
                dp[i][j] = 0

    print(dp)
    return maxlength


# LeetCode 312
def BurstBallons(nums):
    pass

# LeetCode 56
# Greedy Intervals

def mergeIntervals(intervals):

    sorted(intervals)
    left_prev = intervals[0][0]
    right_prev = intervals[0][1]
    array_sol = []

    for i in range(1, len(intervals)):

        left_current = intervals[i][0]
        right_current = intervals[i][1]

        if left_current <= right_prev or right_prev >= right_current:
            minleft = min(left_current, left_prev)
            maxright = max(right_current, right_prev)

            # probably need to check if is not overlapped with the array
            array_sol.append([minleft,maxright])
            left_prev =minleft
            right_prev = maxright

        else:
            array_sol.append([left_current, right_current])

    return array_sol

# LeetCode #3
def LongestSubstringWithoutRepeat(word):

    cache= {}
    maxLenght = 0
    internal_max = 0
    for i in range(len(word)):

        if word[i] not in cache:
            internal_max += 1
            cache[word[i]] = 1
        else:
            maxLenght = max(internal_max, maxLenght)
            internal_max = 1

    print(cache)
    return max(internal_max, maxLenght)


# LeetCode 62
def uniquePath(m, n):
    dp = {}

    def helper(m, n):

        key = (m, n)

        if m == 1 and n == 1:
            return 1

        if m == 0 or n == 0:
            return 0

        if key in dp:
            return dp[key]

        res = helper(m - 1, n) + helper(m, n - 1)
        dp[key] = res
        return res

    result = helper(m, n)
    return result


# LeetCode 1143
def lcs(text1, text2):
    dp = {}

    def helper(i, j):

        if i == len(text1) or j == len(text2):
            return 0

        key = (i, j)

        if key in dp:
            return dp[key]

        if text1[i] == text2[j]:
            res = 1 + helper(i + 1, j + 1)
            dp[key] = res
            return res
        else:
            res = max(helper(i + 1, j), helper(i, j + 1))
            dp[key] = res
            return res

    result = helper(0, 0)
    return result


# LeetCode 1143
def lcsDP(text1, text2):
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp)
    return dp[len(text1)][len(text2)]


# LeetCode 309
# Kind of different DP using 2D matrix,
# colum will be the stage // state of the calculation
def maxProfitDP(prices):
    # [1,2,3,0,2] => 3
    # three stage => for each price: NoStock | sold | in-hand

    noStock = [0] * len(prices)
    sold = [0] * len(prices)
    in_hand = [0] * len(prices)
    in_hand[0] = -prices[0]

    for i in range(1, len(prices)):
        noStock[i] = max(noStock[i - 1], sold[i - 1])
        in_hand[i] = max(in_hand[i - 1], noStock[i - 1] - prices[i])
        sold[i] = in_hand[i - 1] + prices[i]

    # last colum of every array or // last item in each array
    n = len(prices) - 1
    result = max(noStock[n], sold[n])
    return result


# LeetCode 309
def maxProfitBacktracking(prices):
    # max( buy, cooldown )
    # max (sell, cooldown)

    # buy = helper(i+1, not buying) - prices[i]
    # sell = helper(i+2, not buying) + prices[i]

    # cooldown = helper(i+1, buying)

    dp = {}

    def helper(i, buying):

        if i >= len(prices):
            return 0

        key = (i, buying)
        if key in dp:
            return dp[key]

        if buying:
            buy = helper(i + 1, not buying) - prices[i]
            cooldown = helper(i + 1, buying)
            dp[key] = max(buy, cooldown)
        else:
            sell = helper(i + 2, not buying) + prices[i]
            cooldown = helper(i + 1, buying)
            dp[key] = max(sell, cooldown)

        return dp[key]

    result = helper(0, True)
    return result


# LeetCode 518
# 0/1 Knapsack
# select means is amount - coin[i]
# not_select = call function(i+1, coins, amount)
# if amount == 0 means return 1
# if amount < 0 means wrong backtraking way return 0
# sum selec + not_select
def coinChangeIIBack(coins, amount):
    dp = {}

    def helper(i, amount):

        if amount == 0:
            return 1

        if amount < 0:
            return 0

        if i >= len(coins):
            return 0

        key = (i, amount)
        if key in dp:
            return dp[key]

        selected = helper(i, amount - coins[i])
        not_selected = helper(i + 1, amount)

        value = selected + not_selected
        dp[key] = value
        return value

    result = helper(0, amount)
    return result


def targetSum(nums, target):
    max_value = sum(nums)
    dp = {}

    def helper(i, amount):

        if i == len(nums):
            if amount == target:
                return 1
            else:
                return 0

        key = (i, amount)
        if key in dp:
            return dp[key]

        sumar = helper(i + 1, amount + nums[i]) + helper(i + 1, amount - nums[i])
        dp[key] = sumar
        return sumar

    result = helper(0, 0)
    return result


# LeetCode 72
# Given two words find the minimun operation to match both words
# Operations: Insert, Delete, Replace
def editDistance(word1, word2):
    dp = {}

    def helper(i, j):

        if i == len(word1) and j == len(word2):
            return 0

        if i >= len(word1) and j < len(word2):
            return len(word2) - j

        if i < len(word1) and j >= len(word2):
            return len(word1) - i

        key = (i, j)
        if key in dp:
            return dp[key]

        if word1[i] == word2[j]:
            value = helper(i + 1, j + 1)
            dp[key] = value
            return value
        else:
            # replace             #remove           #insert
            value = 1 + min(helper(i + 1, j + 1), helper(i + 1, j), helper(i, j + 1))
            dp[key] = value
            return value

    result = helper(0, 0)
    return result


# LeetCode 97
# "iterating" for each case and use memoization
def interleavingString(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False

    dp = {}

    def helper(i, j, index):

        if i == len(s1) and j == len(s2) and index == len(s3):
            return True

        if i == len(s1) and j != len(s2) and index != len(s3):
            if s2[j] == s3[index]:
                return helper(i, j + 1, index + 1)
            else:
                return False

        if i != len(s1) and index != len(s3) and j == len(s2):
            if s1[i] == s3[index]:
                return helper(i + 1, j, index + 1)
            else:
                return False

        if s1[i] != s3[index] and s2[j] != s3[index]:
            return False

        key = ((i, j), index)
        print(key)

        if key in dp:
            print(f"+key in dp+")
            return dp[key]

        if s1[i] == s3[index] and s2[j] == s3[index]:
            value = helper(i + 1, j, index + 1) or helper(i, j + 1, index + 1)
            dp[key] = value
            return value

        elif s1[i] == s3[index] and s2[j] != s3[index]:
            value = helper(i + 1, j, index + 1)
            dp[key] = value
            return value

        elif s1[i] != s3[index] and s2[j] == s3[index]:
            value = helper(i, j + 1, index + 1)
            dp[key] = value
            return value

    result = helper(0, 0, 0)
    return result


# LeetCode 516
# key is when i > j (translaped iterators) return 0 and i ==j return 1
# not combine i>= j like my first thought
def subpalindromesube(word):
    j = len(word) - 1
    if j == 0:
        return 0
    if j == 1:
        return 1

    memo = {}

    def helper(i, j):

        if i == j:
            return 1

        if i > j:
            return 0

        key = (i, j)
        if key in memo:
            return memo[key]

        # b  c  b
        # i^   j^

        if word[i] == word[j]:
            value = 2 + helper(i + 1, j - 1)
            memo[key] = value
            return value
        else:
            value = max(helper(i + 1, j), helper(i, j - 1))
            memo[key] = value
            return value

    result = helper(0, j)
    return result


# LeetCode 329
# Just I need to check all posibilities (it means -> loop thru each element
# for each element apply dfs in order to start dfs check prev = -inf
# after that prev will be the current element
# memo use two compose for row, col and prev (why the prev because you can going to any elemen from up, down, left, right

def longestIncreasingPath(matrix):
    row = len(matrix)
    col = len(matrix[0])

    maxLengh = 1
    local_max = 0
    prev = float('-inf')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            prev = float('-inf')
            local_max = dfs(matrix, i, j, prev)
            if local_max > maxLengh:
                maxLengh = local_max

            #       print(f"local_max:", local_max)
            #       print("<________________________________>")
            local_max = 0
            print(visited)

    print("maxLengh:", maxLengh)
    return maxLengh


visited = {}


def dfs(matrix, row, col, prev):
    if row == len(matrix) or col == len(matrix[0]):
        return 0

    if row < 0 or col < 0:
        return 0

    # print(f"matrix:", matrix[row][col])
    # print(f"prev: ", prev)

    key = ((row, col), prev)
    if key in visited:
        print(f"[{row}][{col}]: ", matrix[row][col])
        return visited[key]

        # movements
        # up = row-1, col
        # down = row+1, col
        # right = row, col+1
        # left = row, col-1

    if matrix[row][col] > prev:
        value = 1 + max(dfs(matrix, row - 1, col, matrix[row][col]), dfs(matrix, row + 1, col, matrix[row][col]),
                        dfs(matrix, row, col + 1, matrix[row][col]), dfs(matrix, row, col - 1, matrix[row][col]))
        visited[key] = value
        return value
    else:
        return 0


def longestIncreasingPathDP(matrix):
    dp = [[1] * len(matrix[0]) for _ in range(len(matrix))]

    prev = float('-inf')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            prev = float('-inf')
            dp[i][j] = dfsDP(matrix, i, j, prev, dp)


def dfsDP(matrix, row, col, prev):
    if row == len(matrix) or col == len(matrix[0]):
        return 0

    if row < 0 or col < 0:
        return 0

    if matrix[row][col] > prev:
        return 1 + max()

    else:
        return 0


if __name__ == '__main__':

    nums = [3, 1, 5, 8]
    envelopes = [[1,1],[1,1],[1,1]]
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    word = "dvdf"
    a = [2,1,1]
    b = [1,2,3]
    m = 4
    n = 7
    text1 = "intention"
    text2 = "execution"
    prices = [1, 2, 4]
    coins = [10]
    amount = 10
    target = 3
    word1 = "abc"
    word2 = "abc"
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]

    print(longestIncreasingPath(matrix))
