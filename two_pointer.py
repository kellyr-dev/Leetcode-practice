import heapq


# 11. Container With Most Water (not checked)
def maxArea(height):

    if len(height) <= 1:
        return 0

    left = 0
    right = 1
    max_area = 0
    min_height = float('inf')

    while right < len(height)-1:

        base = right - left
        if height[right] < min_height:
            min_height = height[right]

        area = base * min_height
        if area > max_area:
            max_area = area

        right += 1

    while left < len(height)-1:
        base = right - left
        if height[right] < min_height:
            min_height = height[right]

        area = base * min_height
        if area > max_area:
            max_area = area

        left += 1

    return max_area

# 28. Find the Index of the First Occurrence in a String
def strStr(haystack, needle):

    ned_pointer = 0
    hay_pointer = 0
    result = -1
    queue = []

    if len(needle) > len(haystack):
        return -1

    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            queue.append(i)

    print(queue)
    print(len(needle))
    while hay_pointer < len(haystack):

        #   print(needle[ned_pointer])
        if haystack[hay_pointer] == needle[ned_pointer]:
            if ned_pointer == 0:
                result = hay_pointer
            ned_pointer += 1
        else:
            ned_pointer = 0
            result = -1
            if len(queue) > 1:
                hay_pointer = queue.pop(0)

        if ned_pointer == len(needle)-1:
            return result

        hay_pointer += 1

    return result

# Caesar Cipher hackerank
def caesarCipher(s, k):
    #rangeMleft = 65
    #rangeMright = 90
    #rangemleft = 97
    #rangemright = 122
    news = []

    for i in range(len(s)):
        if s[i].isalpha():
            value = ord(s[i])
            print(value)

            if value >= 65 and value <= 90:

                if (value + k) <= 90:
                    news.append(chr(value +k))
                else:
                    value = value + k
                    while (value) > 90:
                        print(f"(value +k)", (value))
                        resto = (value) - 90
                        value = 65 + resto - 1
                        print(f" new value: ",value)

                    news.append(chr(value))

            if value >= 97 and value <= 122:

                if (value + k) <= 122:
                    news.append(chr(value + k))
                else:
                    value = value + k
                    while (value) > 122:
                        print(f"(value +k)", (value))
                        resto = (value) - 122
                        value = 97 + resto - 1
                        print(f" new value: ",value)
                    news.append(chr(value))
        else:

            news.append(s[i])

    print(news)
    what_is =''.join(map(str, news))
    print(what_is)
    return what_is

def dividir(endo, sor):

    INFINITY = 2147483646
    ZERO = -2147483648

    # some edge cases
    if endo == sor:
        return 1

    # considering sor like infinity
    if sor == INFINITY:
        return 0

    # considering endo like 0
    if endo == ZERO:
        return 0

    if endo >= INFINITY:
        return INFINITY

    if sor == ZERO:
        return INFINITY

    flagSor = False
    flagEndo = False

    if sor < 0:
        flagSor = True
        cont = 0
        while sor < 0:
            sor = sor + 1
            cont += 1
            print(f"sor: ", sor)
            print(f"cont: ",cont)

        sor = cont
        print(f"new_sor: ", sor)

    if endo <0:
        flagEndo = True
        cont = 0
        while endo < 0:
            endo = endo + 1
            cont += 1
            print(f"endo: ", endo)
            print(f"cont: ", cont)

        endo = cont

    suma = 0
    resto = endo
    result = 0

    while resto >= sor:
        suma = suma + sor
        resto = resto - sor
        result+= 1

        print(f"suma: ", suma)
        print(f"resto: ", resto)
        print(f"result: ", result)

    if flagEndo and flagSor:
        return result

    if flagEndo or flagSor:
        # result * -1
        cont = 0
        while result > 0:
            result = result - 1
            cont += 1

        while cont > 0:
            result = result - 1
            cont -= 1

    return result

# 567. Permutation in String
def permutationString(s1, s2):

    # corner cases
    if len(s1) > len(s2):
        return False

    if len(s1) == 0:
        return True

    if len(s2) == 0:
        return False

    if len(s1) == len(s2):
        aux1 = ''.join(sorted(s1))
        aux2 = ''.join(sorted(s2))
        if aux1 == aux2:
            return True
        else:
            return False

    hasmap = {}
    right = len(s1) -1
    left = 0
    index = 0
    flag = False

    while right < len(s2): #O(n)

        for i in range(len(s1)): # O(m)
            if s1[i] in hasmap:
                hasmap[s1[i]] += 1
            else:
                hasmap[s1[i]] = 1
        print(hasmap)

        while left <= right:
            if s2[left] in hasmap:
                hasmap[s2[left]] -= 1
            left += 1

        for value in hasmap.values():
            if value != 0:
                flag = True
                break

        if flag:
            print(hasmap)
            index += 1
            left = index
            right += 1
            hasmap.clear()
            flag = False
        else:
            return True


    return False
    # O(mn) being m = lenght of s1 // n = lenght of s2

# 713. Subarray Product Less Than K
def numSubarrayProductLessThanK(nums, target):

    index = 0
    right = 0
    product = 1
    left = 0
    result = []
    aux_product = 1

    # initialization
    while right < len(nums):

        product = product * nums[right]
        if product > target:

            for i in range(left, right):
                for j in range(left + 1, right + 1):
                    aux_product = nums[i] * nums[j]
                    print(f"nums[i] * nums[j]", nums[i], nums[j])
                    if aux_product < target:
                        result.append([nums[i], nums[j]])

            product = product / nums[index]
            aux_product = 1
            print(f"new product: ", product)
            print(f"index: ", index)
            index += 1

        right += 1

    return result

# 26. Remove Duplicates from Sorted Array
def removeDuplicates(nums):

    count = 1
    if len(nums) <= 1:
        return len(nums)

    left = 0
    right = 1

    while right < len(nums):
        if nums[right] == nums[left]:
            nums[right] = "_"
            right += 1
        else:
            left = right
            right += 1
            count += 1

    print(f"nums: {nums}")
    right = 0
    reachFinal = False
    for left in range(len(nums)):
        if nums[left] == "_":
            if left + 1 <= len(nums) - 1:
                right = left + 1
                while reachFinal == False and nums[right] == "_":
                    right += 1
                    if right > len(nums) - 1:
                        reachFinal = True

                if reachFinal == True:
                    continue
                else:
                    aux = nums[left]
                    nums[left] = nums[right]
                    nums[right] = aux
                    reachFinal = False
    print(nums)
    return count

# 977. Squares of a Sorted Array
def sortedSquares(nums):

    #result = [0 for i in range(len(nums))]
    result = [0] * len(nums)
    left = 0
    right = len(nums) - 1
    index = len(nums) - 1

    while left <= right and index >= 0:

        leftSide = nums[left]*nums[left]
        rightSide = nums[right]*nums[right]

        if rightSide > leftSide:
            result[index] = rightSide
            index -= 1
            right -= 1
        else:
            result[index] = leftSide
            index -= 1
            left += 1

    return result

# 15. 3Sum
def s3um(nums):

    result = []
    nums.sort()
    table_hash = {}

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        else:

            left = i+1
            right = len(nums)-1
            tgt = nums[i]*-1
            print(f"tgt: {tgt}")
            while left < right:
                if nums[left] + nums[right] == tgt:
                    key = (nums[i], nums[left], nums[right])
                    if key not in table_hash:
                        result.append([nums[i], nums[left], nums[right]])
                        table_hash[key] = True
                    left += 1
                elif nums[left] + nums[right] > tgt:
                    right -= 1
                else:
                    left += 1

    return result

# 16. 3Sum Closest
def s3umClosest(nums, target):

    if len(nums) <= 2:
        return 0

    if len(nums) == 3:
        return nums[0] + nums[1] + nums[2]

    nums.sort()
    smallestPos = []

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1

        while left < right:

            localSum = nums[i] + nums[left] + nums[right]
            if localSum - target == 0:
                return nums[i] + nums[left] + nums[right]

            elif localSum > target:
                val = abs(localSum - target)
                key = (val, localSum)
                right -= 1
                heapq.heappush(smallestPos, key)
            else:
                val = abs(localSum - target)
                key = (val, localSum)
                left += 1
                heapq.heappush(smallestPos, key)

    return heapq.heappop(smallestPos)[1]


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]

    stringCheck = "abcdefghijklmnopqrstuvwxyz"
    k = 2
    endo = 7
    sor = -3
    s1 = "ab"
    s2 = "ba"
    nums = [1,1,1,1]
    target = 3
    print(s3umClosest(nums, target))
