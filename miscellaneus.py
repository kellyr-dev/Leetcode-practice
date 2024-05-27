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


if __name__ == '__main__':
    word = "ballon"
    nums = [1, 3, 5, 12, 11, 12, 11]
    k = 2
    print(topKFrequent(nums, k))
