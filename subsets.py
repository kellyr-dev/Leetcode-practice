
# 78. Subsets
def find_subsets(nums):

    result = [[]]
    if len(nums) == 0:
        return result
    elif len(nums) == 1:
        result.append([nums[0]])
        return result
    elif len(nums) == 2:
        result.append([nums[0]])
        result.append([nums[1]])
        result.append([nums[0], nums[1]])
    else:
        for i in range(len(nums)):
            print(f"result: {result}")
            print(f"i: {i}")
            n = len(result)
            for j in range(n): #O(2^n)
                aux = list(result[j])
                print(f"aux: {aux}")
                aux.append(nums[i])
                result.append(aux)


    return result

# 90. Subsets II
def subsetsWithDup(nums):
    result = [[]]
    aux_hash = {}
    for i in range(len(nums)):

        n = len(result)
        for j in range(n):

            aux = list(result[j])
            aux.append(nums[i])
            key = tuple(aux)
            print(f"key: {key}")
            if key not in aux_hash:
                result.append(aux)
                aux_hash[key] = 1

    return result

# 784. Letter Case Permutation
def findLetterCaseStringPermutations(letters):

    aux_result = [[]]

    for i in range(len(letters)):
        n = len(aux_result)
        for j in range(n):

            if letters[i].isnumeric():
                aux_result[j].append(letters[i])
            else:
                letterCap = ""
                if letters[i].islower():
                    letterCap += letters[i].capitalize()
                else:
                    letterCap += letters[i].lower()

                letter = letters[i]

                aux1 = list(aux_result[j])
                aux2 = list(aux_result[j])
                aux1.append(letterCap)
                aux2.append(letter)

                aux_result[j] = aux1
                aux_result.append(aux2)

    print(aux_result)

    result = []

    for array_letter in aux_result:
        aux = "".join(array_letter)
        result.insert(0,aux)

    return result

#22. Generate Parentheses
def generateParenthesis(n):

    if n == 0:
        return [""]

    if n == 1:
        return ["()"]
    if n == 2:
        return ["(())", "()()"]

    newn = n*2
    result = ['(']
    table_hash = {'(': (1,0)}
    for i in range(newn):
        lenght = len(result)
        for j in range(lenght):

            auxOpen = table_hash[result[j]][0]
            auxClose = table_hash[result[j]][1]
            strinCase = result[j]
            #table_hash.pop(strinCase)

            if auxOpen < n:
                if auxOpen == auxClose:
                    # only can add '('
                    strinCase += '('
                    key = (auxOpen+1, auxClose)
                    result[j] = strinCase
                    table_hash[strinCase] = key
                elif auxOpen > auxClose:
                    # must be the normal case add '(' and ')'
                    auxStrOpen = strinCase + '('
                    auxStrClose = strinCase + ')'
                    keyOpen = (auxOpen + 1, auxClose)
                    keyClose = (auxOpen, auxClose + 1)

                    table_hash[auxStrOpen] = keyOpen
                    table_hash[auxStrClose] = keyClose

                    result[j] = auxStrOpen
                    result.append(auxStrClose)

            elif auxOpen == n:
                if auxOpen == auxClose:
                    # continue is ok
                    continue
                    #key = (auxOpen, auxClose)
                    #table_hash[strinCase] = key
                elif auxClose < auxOpen:
                    # only can add ')'
                    strinCase += ')'
                    result[j] = strinCase
                    key = (auxOpen, auxClose + 1)
                    table_hash[strinCase] = key

    print(len(result))
    return result

# Evaluate Expressuion and return all values possibles
def diffWaysToEvaluateExpression(s):

    result = []

if __name__ == '__main__':

    nums = [1, 3, 5]
    letters = "ad52"
    n = 5
    print(generateParenthesis(n))
