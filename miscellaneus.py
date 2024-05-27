import re


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

def Ginterview(string):

    new_string = []
    prev_star = string.split("(")
    if len(prev_star) > 1:
        inside = prev_star[1].split(")")
        if len(inside) > 1:
            new_string.append(prev_star[0])
            new_string.append(inside[0])
            new_string.append(inside[1])
        else:
            new_string.append(prev_star[0])
            new_string.append(inside[0])
    else:
        new_string.append(prev_star[0])

    print(new_string)

    #if len(new_string) == 3:
        # apply complete algorithm
        # just put new_string[0] in a hashmap
        # after that multiply new_string[3][0] if a number * new_string[2]
        # check if multiply exist in hashmap
        # after that += add or add

    return new_string

if __name__ == '__main__':
    word = "ballon"
    nums = [1, 3, 5, 12, 11, 12, 11]
    k = 2
    string = "H2(MgO2)2"
    print(Ginterview(string))
