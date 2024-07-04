import re, heapq


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

    col = len(matrix)
    row = len(matrix[0])
    # 9 - k = x
    # 8 / 3 =
    print(col)
    print(row)


    for i in range(len(matrix)):

        aux.append(matrix[i])
    print(aux)
    return -1

if __name__ == '__main__':
    word = "ballon"
    nums = [5, 12, 11, -1, 12]
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8

    string = "O4(H2O)2O2" #=> H4, 08
    print(kthSmallestMatrix(matrix, k))
