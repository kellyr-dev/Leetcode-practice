import re, heapq, math


# 1189. Maximum Number of Balloons -> HASHMAP
def maxNumberOfBalloons(word):
    table = {
        "b": 0,
        "a": 0,
        "l": 0,
        "o": 0,
        "n": 0
    }

    for i in range(len(word)):

        if word[i] in table:
            table[word[i]] += 1

    factor = float('inf')
    print(f"table: {table}")

    for value in table:
        if value == 'l' or value == '0':
            factor = min(table[value] // 2, factor)
        else:
            factor = min(table[value], factor)

    return factor

def nextLargerElement(nums):
    res = [-1] * len(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                res[i] = nums[j]
                break
    print(res)
    return res

def converToBinary(num):
    divisor = num
    stack = []

    while divisor > 0:
        resto = divisor % 2
        stack.insert(0, str(resto))
        divisor = divisor // 2
    result = ""
    for i in range(len(stack)):
        result += stack[i]

    return result

def sortInplace(nums):
    table = {}

    for i in range(len(nums)):
        table[nums[i]] = i

    print(table)

    for i in range(len(table)):

        if i not in table:
            return i

# 347. Top K Frequent Elements
def topKFrequent(nums, k):
    hashing = {}

    for i in range(len(nums)):
        if nums[i] in hashing:
            hashing[nums[i]] += 1
        else:
            hashing[nums[i]] = 1

    ordered = sorted(hashing.items(), key=lambda item: item[1], reverse=True)
    print(ordered)

    result = []

    for i in range(k):
        result.append(ordered[i][0])

    return result

def elmentEval(string):

    # GInterview SOLVED
    """
    # Given an string of periodelment divide it in parts
    # H2O => H2, O1
    # HMg => H, Mg
    # H2(MgO2)2 => H2, Mg2, O4
    # O4(H2O)2 => H4, O6
    # O4(H2O)2O2 => H4, O8 """

    # First/Original approach
    i = 0
    left = 0
    hashmap = {}
    stacks_of = []

    while i < len(string):
        #print(f"i:{i} -> {string[i]} => {stacks_of} => {hashmap}")

        #if char is a digit() or is a lower letter
        if string[i].isdigit() or string[i].islower():  # condition to put into hashmap
            if len(stacks_of) > 0:  # if some element are in the stack

                while stacks_of:  # poping from the stack until is empty
                    aux_key = stacks_of.pop(0)
                    aux_key_letter = aux_key[0]
                    aux_key_number = aux_key[1] * int(string[i])

                    if aux_key_letter in hashmap:
                        hashmap[aux_key_letter] += aux_key_number
                    else:
                        hashmap[aux_key_letter] = aux_key_number
            elif string[i].islower():
                aux = ""+string[i-1]+string[i]

                if aux in hashmap:
                    hashmap[aux] += int(string[i])
                else:
                    hashmap[aux] = 1
            else:
                value = int(string[i])
                aux = string[i-1]

                if aux in hashmap:
                    hashmap[aux] += value
                else:
                    hashmap[aux] = value


            i += 1
            left = i #i

        #if char is open parethesis
        elif string[i] == "(":

            i += 1  # move to next char because string[i] is equal to "("
            left = i

            while i < len(string) and string[i] != ")":
                if string[i].isdigit():
                    key = (string[left:i], int(string[i]))  # if it is a digit I have case "O2"
                    stacks_of.append(key)
                    i += 1
                    left = i
                elif string[i].islower():  # if it is a lowerletter  I have case "Mg" it means (Mg,1)
                    key = (string[left:i + 1], 1)
                    stacks_of.append(key)
                    i += 1
                    left = i
                else:
                    i += 1

            if i - left >= 1:
                key = (string[left:i], 1)
                stacks_of.append(key)

        #if it is capitalize letter # check next letter if it is a lowercase
        else:
            if i+1 < len(string):
                if string[i+1].isupper():
                    if string[i] in hashmap:
                        hashmap[string[i]] += 1
                    else:
                        hashmap[string[i]] = 1
                i += 1

            else:
                if string[i] in hashmap:
                    hashmap[string[i]] += 1
                else:
                    hashmap[string[i]] = 1
                i += 1


    print(hashmap)
    res = []
    for key in hashmap:
        word = "" + key + str(hashmap[key])
        res.append(word)

    res.sort()
    return res

def topKagain(nums, k):

    if k > len(nums):
        return []

    for i in range(len(nums)):
        nums[i] = nums[i] * -1

    heapq.heapify(nums)
    aux = []
    for i in range(k):
        value = heapq.heappop(nums)
        print(f"value: ", value)
        aux.append(value)

    for i in range(len(aux)):
        aux[i] = aux[i] * -1
    return aux

# Kth Smallest Number (easy)
def kthSmallestNumber(nums, k):

    if k > len(nums):
        k = len(nums)

    heapq.heapify(nums)

    for i in range(k):
        value = heapq.heappop(nums)

    return value

# 378. Kth Smallest Element in a Sorted Matrix
def kthSmallestMatrix(matrix, k):

    aux = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            aux.append(matrix[i][j])

    heapq.heapify(aux)
    value = -1
    for i in range(k):
        value = heapq.heappop(aux)

    return value

# 973. K Closest Points to Origin
def kClosestPointsTotheOrigin(points, k):

    result = []
    table_hash = {}

    if k >= len(points):
        return points

    for i in range(len(points)):  # O(n)

        suma = pow(points[i][0],2) + pow(points[i][1],2)
        value = math.sqrt(suma)
        result.append(value)

        if value in table_hash:
            table_hash[value].append([points[i][0],points[i][1]])
        else:
            table_hash[value] = [[points[i][0],points[i][1]]]

    print(table_hash)
    heapq.heapify(result)
    ans = []
    j = 0

    while j < k:  # k*log(n)
        print(f"j: {j}")
        value = heapq.heappop(result)
        array_ = table_hash[value]
        if len(array_) > 1:
            for i in range(len(array_)):
                if j < k:
                    ans.append(array_[i])
                    j+= 1
                else:
                    break
        else:
            ans.append(array_[0])
            j += 1

    return ans

# Connect Ropes
def minimumCostToConnectRopes(nums):

    if len(nums) == 1:
        return nums[0]

    if len(nums) == 0:
        return 0

    heapq.heapify(nums) # O(n)

    result = 0
    while len(nums) > 1:
        num1 = heapq.heappop(nums) # O(Log(n))
        num2 = heapq.heappop(nums) # O(Log(n))
        suma = num1 + num2
        print(f"(num1:{num1} - num2:{num2}) => suma: {suma}")
        heapq.heappush(nums, suma)

        result = result + suma

    return result

# 347. Top K Frequent Elements
def topKFrequent(nums, k):

    hashing = {} # O(n) -> memory
    for num in nums: # O(n) -> time
        hashing[num] = hashing.get(num, 0) + 1 # if num in hashing; hashing[num] += 1 else hashing[num] = 1

    minHeap = [] # O(n) -> memory

    for num, frequency in hashing.items(): # O(n) * O(log(n)) -> time
        heapq.heappush(minHeap, (frequency, num))
        print(f"minHeap: {minHeap}")
        if len(minHeap) > k:
            heapq.heappop(minHeap)

    print(minHeap)
    result = []
    while minHeap: # O(k) * O(log(k))
        result.append(heapq.heappop(minHeap)[1])

    return result

# 347. Top K Frequent Elements
def topKfrequentWithoutHeap(nums, k):

    table_hash = {} # O(n) -> memory
    for i in range(len(nums)):

        if nums[i] in table_hash: # O(n) -> time

            print(table_hash[nums[i]][0])
            key = (int(table_hash[nums[i]][0])+1, nums[i])
            table_hash[nums[i]] = key
        else:
            key = (1, nums[i])
            table_hash[nums[i]] = key

    ordered = sorted(list(table_hash.values()), reverse=True) # O(nlog(n)) -> time and O(n) memory
    print(ordered)


    result = [] # O(k)
    for i in range(k): # O(k)
        result.append(ordered[i][1])

    return result

    # Time Complexity = O(n) + O(nlog(n)) + O(k) = O(nlog(n))
    # Memory = O(n) + O(n) + O(k) = 2*O(n) + O(K) = O(n)

# 658. Find K Closest Elements
def findClosestElements(nums, k, x):

    minHeap = []

    for num in nums:
        value = (abs(num - x), num)
        minHeap.append(value)

    heapq.heapify(minHeap)

    result = []
    for i in range(k):
        result_ith = heapq.heappop(minHeap)
        result.append(result_ith[1])

    result.sort()
    return result

# find distinct elements k
def findMaximumDistinctElements(nums, k):

    table_hash = {}
    for num in nums: # O(n)
        # key = (freq, num)
        if num in table_hash:
            key = (int(table_hash[num][0])+1, num)
            table_hash[num] = key
        else:
            key = (1, num)
            table_hash[num] = key

    print(table_hash)

    distint = []
    maxHeap = []

    for pair in table_hash.values(): # O(n)
        if pair[0] == 1:
            distint.append(pair[1])
        else:
            maxHeap.append(pair)

    print(distint)
    heapq.heapify(maxHeap) # O(n)
    print(maxHeap)

    while k > 0 and len(maxHeap) > 0: #k*log(n)
        value = heapq.heappop(maxHeap)
        print(f"value: {value}")
        if value[0] == 2:
            distint.append(value[1])
        else:
            key = (value[0]-1, value[1])
            heapq.heappush(maxHeap, key)

        k -= 1

    if k > 0:
        print(distint)
        return len(distint) - k
    else:
        print(distint)
        return len(distint)

# find sum between k1 and k2
def findSumOfElements(nums, k1, k2):

    if k1 < 0 or k2 < 0:
        return -1

    if k1 == k2:
        return 0

    heapq.heapify(nums)

    for i in range(k1):
        heapq.heappop(nums)

    print(nums)
    result = 0
    k2 = (k2 - k1) -1
    print(k2)
    for j in range(k2):
        result += heapq.heappop(nums)

    return result

# 767. Reorganize String (not checked)
def rearrangeString(str1):

    print(f"String: {str1}")
    table_hash = {}
    l = 0
    r = 1
    while r < len(str1):

        print(f"table_hash: {table_hash}")
        print(f"l: {l} -> r: {r}")
        if str1[r] == str1[l]:
            while r < len(str1) and str1[r] == str1[l]:
                r += 1

            aux = []
            for _ in range(l, r):
                aux.append(_)
            print(f"aux: {aux}")

            if str1[l] in table_hash:
                _aux = list(table_hash[str1[l]])
                for val in aux:
                    _aux.append(val)
                table_hash[str1[l]] = _aux
            else:
                table_hash[str1[l]] = aux

            for j in range(len(aux)-1):
                for char in table_hash:
                    if str1[l] != char:
                        tmp = table_hash[char].pop(0)
                        table_hash[char].append(aux[j])
                        aux[j] = tmp
                        break
            l = r
            r += 1
            # make algorithm to swap

        else:
            if str1[l] in table_hash:
                _aux = table_hash[str1[l]]
                _aux.append(l)
                table_hash[str1[l]] = _aux
            else:
                table_hash[str1[l]] = [l]

            r += 1
            l += 1

    if l < len(str1):
        if str1[l] in table_hash:
            _aux = table_hash[str1[l]]
            _aux.append(l)
            table_hash[str1[l]] = _aux
        else:
            table_hash[str1[l]] = [l]

    print(table_hash)
    result = list(str1)
    #print(result)

    for char in table_hash:
        print(f"char: {char}")
        lista = table_hash[char]
        for values in lista:
            print(f"values: {values}")
            result[values] = char

    result_str = "".join(list(result))
    print(result_str)

    return list(table_hash.values())

# 621. Task Scheduler
def leastIntervalI(tasks, n):
    table_hash = {}

    for value in tasks:

        if value in table_hash:
            key = (table_hash[value][0] - 1, value)
            table_hash[value] = key
        else:
            key = (-1, value)
            table_hash[value] = key

    freq_values = list(table_hash.values())
    heapq.heapify(freq_values)
    cycle = 0

    while freq_values:
        waitlist = []
        k = n + 1 # k = 2+1
        while k > 0 and freq_values:
            cycle += 1
            pair = heapq.heappop(freq_values)
            print(f"pair: {pair}")
            if -pair[0] > 1:
                key = (pair[0]+1, pair[1])
                waitlist.append(key)
            k -= 1

        for pairs in waitlist:
            heapq.heappush(freq_values, pairs)

        if freq_values:
            cycle = cycle + k # 2 + 1



    return cycle

# 409. Longest Palindrome
def longestPalindrome(s):

    hash_table = {}
    for i in range(len(s)):
        if s[i] in hash_table:
            hash_table[s[i]] += 1
        else:
            hash_table[s[i]] = 1


    maxOdd = -1
    countNotOdd = 0

    for value in hash_table.values():
        print(f"value: {value}")
        if value % 2 == 0:
            countNotOdd += value
        else:
            if value > maxOdd:
                if maxOdd != -1:
                    countNotOdd += maxOdd - 1
                    maxOdd = value
                else:
                    maxOdd = value
            else:
                countNotOdd += value-1

    if maxOdd != -1:
        return maxOdd + countNotOdd
    else:
        return countNotOdd

# 383. Ransom Note
def canConstruct(ransomNote, magazine):

    hash_of_ransom = {}
    for i in range(len(ransomNote)):
        if ransomNote[i] in hash_of_ransom:
            hash_of_ransom[ransomNote[i]] += 1
        else:
            hash_of_ransom[ransomNote[i]] = 1

    for i in range(len(magazine)):
        if magazine[i] in hash_of_ransom:
            if hash_of_ransom[magazine[i]] > 0:
                hash_of_ransom[magazine[i]] -= 1

    suma_of_letters = sum(hash_of_ransom.values())

    if suma_of_letters > 0:
        return False
    else:
        return True



if __name__ == '__main__':
    word = "ballon"
    nums = [3, 5, 8, 7]
    k1 = 1
    k2 = 4
    x = 7
    matrix = [[1, 3], [3, 4], [2, -1]]
    string = "O4(H2O)2O2" #=> H4, 08
    str1 = "Programmingg"

    tasks = ["A","A","A","B","B","B"]
    n = 2
    arr = [1,3,5,6,7,8,11,13,14,16,17,18,19,20,21,23,24,25,26,28,29,30,31,34,35,36,37,38,41,43,44,47,50,51,53,54,56,57,58,59,60,62,63,65,67,68,69,70,71,72,73,74,76,78,80,81,83,84,85,88,89,90,91,92,93,95,97,98,102,103,104,105,108,109,110,111,112,113,114,117,120,123,124,125,127,128,129,130,131,132,133,135,136,137,138,139,141,142,145,146,148,149,150,151,153,154,155,156,161,162,164,167,168,169,170,171,172,175,176,178,179,181,182,184,191,193,195,196,199,201,202,204,205,208,210,214,215,217,219,221,222,224,226,228,229,230,231,232,234,235,236,240,242,246,248,249,251,252,253,254,255,256,257,258,259,260,261,262,265,267,269,272,273,275,278,279,280,281,282,283,284,285,286,287,289,291,292,293,296,297,298,299,303,305,306,308,312,313,315,316,318,320,323,324,327,330,332,335,337,340,342,343,344,346,349,350,352,353,354,356,357,359,360,362,366,367,369,370,374,375,376,377,378,379,382,384,386,390,392,393,394,395,396,399,400,401,403,406,411,413,415,416,420,424,425,426,427,429,430,432,434,435,436,437,438,439,440,441,442,443,444,446,447,448,449,452,455,456,458,459,460,461,462,463,464,465,466,467,469,470,471,472,477,479,480,483,484,486,488,489,490,491,492,493,494,495,500,501,503,504,506,508,510,513,514,515,516,517,527,531,533,534,535,536,542,543,546,547,548,549,550,553,556,559,561,562,563,566,567,569,571,572,576,578,579,581,582,583,584,586,589,591,592,593,594,595,598,600,601,602,603,605,606,607,609,611,612,613,614,616,617,621,622,624,625,626,627,630,631,633,635,636,637,639,640,643,644,646,647,648,649,650,651,652,654,658,660,661,662,663,664,665,667,668,669,672,673,678,679,683,685,686,687,689,690,691,692,693,695,696,697,701,702,703,704,707,709,711,714,717,718,719,720,721,723,724,725,726,728,729,730,733,735,736,737,738,740,742,745,746,747,750,754,755,757,759,761,763,765,768,771,773,774,775,776,779,780,781,782,783,784,787,788,789,790,791,792,794,795,797,798,800,801,805,806,808,810,811,812,814,816,819,822,824,825,826,828,831,833,835,838,841,842,844,845,846,847,849,853,854,855,857,858,861,862,866,868,869,870,874,878,882,884,885,888,889,890,892,893,897,900,903,905,906,907,908,911,913,916,918,920,921,922,924,925,926,928,929,930,932,933,934,936,937,938,940,942,944,946,949,953,954,956,957,958,961,962,964,965,966,969,972,973,974,976,977,978,979,980,981,982,984,985,986,988,993,996,997,999]
    k = 724
    strs = ["dog","racecar","car"]
