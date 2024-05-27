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

# Given an string of periodelment divide it in parts
# H2O => H2, O1
# HMg
# H2(MgO2)2 => H2, Mg2, O4
# O4(H2O)2 => H4, O6
# O4(H2O)2O2 => H4, O8

# First/Original approach
def elmentEval(string):
    i = 0
    left = 0
    hashmap = {}
    stacks_of = []

    while i < len(string):
        print(f"i:{i} -> {string[i]}")

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
            else:
                aux = string[left:i]
                if aux in hashmap:
                    hashmap[aux] += int(string[i])
                else:
                    hashmap[aux] = int(string[i])

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

        #if it is capitalize letter
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

    '''
    if i - left >= 1:  # if the last element is an element without number like just: "O"
        final_element = string[left:i]
        if final_element in hashmap:
            hashmap[final_element] += 1
        else:
            hashmap[final_element] = 1
    '''

    print(hashmap)
    res = []
    for key in hashmap:
        word = "" + key + str(hashmap[key])
        res.append(word)

    res.sort()
    return res
if __name__ == '__main__':
    word = "ballon"
    nums = [1, 3, 5, 12, 11, 12, 11]
    k = 2
    string = "H2(MgO2)2"
    print(elmentEval(string))
