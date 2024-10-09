# key is to identify when is DP or Greedy
def findboatppl(nums, limit):
    left = 0
    right = len(nums) - 1
    nums.sort()

    boat = 0
    while left < len(nums) and left < right:
        if nums[right] + nums[left] <= limit:  # be greedy with left
            left += 1

        right -= 1
        boat += 1

    if left == right:
        boat += 1

    return boat


# 680. Valid Palindrome II
def helperPalidrome(aux, l, r):
    print(f"aux: {aux}")

    while l < r:
        if aux[l] != aux[r]:
            return False
        l += 1
        r -= 1

    return True


def validPalindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        print(f"({l}:{r})")
        print(f"s[l]:{s[l]} <-> s[r]:{s[r]}")

        if s[l] != s[r]:
            return helperPalidrome(s, l + 1, r) or helperPalidrome(s, l, r - 1)
        l += 1
        r -= 1
    return True


# 646. Maximum Length of Pair Chain
def findLongestChain(pairs):
    pairs.sort(key=lambda item: item[1])
    maxCount = 1
    j = 1
    i = 0

    while j < len(pairs):
        if pairs[i][1] < pairs[j][0]:
            maxCount += 1
            i = j

        j += 1

    return maxCount


# 921. Minimum Add to Make Parentheses Valid
def minAddToMakeValid(S):
    stacks = []
    j = 0
    while j < len(S):
        print(f"{stacks} => S[j]: {S[j]}")
        if S[j] == "(":
            stacks.append("(")
        else:
            if len(stacks) > 0:
                tam = len(stacks) - 1
                if stacks[tam] == "(":
                    stacks.pop(tam)
                else:
                    stacks.append(")")
            else:
                stacks.append(")")
        j += 1

    return len(stacks)


# 316. Remove Duplicate Letters (no Checked)
def removeDuplicateLetters(s):

    alphabet = [0] * 26
    table_hash = {}
    result_array = []
    i = 0

    while i < len(s): # O(n)

        if s[i] in table_hash:

            # if Char already in hasmap then check if there is a Char in the alphabet before it
            limit = (ord(s[i])+ 1) - 97
            flag = False
            for j in range(limit):  # lees than 26 it means is constant O(26) "teorically"
                if alphabet[j] != 0:
                    print(f"alphabet[j]: {alphabet[j]} => s[j]:{s[i]}" )
                    rank = table_hash[alphabet[j]]
                    if rank[0] > table_hash[s[i]][0]:
                        flag = True
                        break

            if flag:
                key = (i, s[i])
                table_hash[s[i]] = key

        else:
            table_hash[s[i]] = (i, s[i])
            index = ord(s[i]) - 97
            alphabet[index] = s[i]

        i += 1

    result_array = list(table_hash.values()) # O(n)
    result_array.sort() # O(nlog(n) -> sorted by i

    result = []
    for pair in result_array:
        result.append(pair[1])

    return "".join(list(result))

# 2384. Largest Palindromic Number (no Checked)
def largestPalindromic(string):

    table_hash = {}
    # check freq, numbers
    for i in range(len(string)): # O(n)
        if string[i] != '0':
            if string[i] in table_hash:
                key = (table_hash[string[i]][0]+1, string[i])
                table_hash[string[i]] = key
            else:
                table_hash[string[i]] = (1, string[i])

    compose = list(table_hash.values())
    compose.sort(reverse=True) # O(n(log(n))

    if len(compose) == 0:
        return ""

    if compose[0][0] == 1:
        return compose[0][1]

    array_pre = []

    # two ways to build and depure array
    if compose[0][0] % 2 == 0: # max value is odd, we need at leats one impar

        cont = 0
        maxValues = 0
        for value in compose:
            if value[0] > 1:
                array_pre.append(value)
                maxValues += value[0]
            else:
                if cont < 1:
                    array_pre.append(value)
                    cont += 1
                    maxValues += value[0]
    else:
        cont = 0
        maxValues =0

        for value in compose:
            if value[0] >= 2:
                if value[0] % 2 == 0:
                    array_pre.append(value)
                    maxValues += value[0]
                else:
                    if cont < 1:
                        array_pre.append(value)
                        maxValues += value[0]
                        cont += 1
                    else:
                        key = (value[0]-1, value[1])
                        array_pre.append(key)
                        maxValues += key[0]

    # build the result
    print(f"final: {array_pre}")
    print(f"maxValues: {maxValues}")
    result = [0] * maxValues
    print(f"result: {result}")
    l = 0
    r = len(result)-1
    while l < r:
        freq = array_pre.pop(0)

        if freq[0] % 2 == 0:
            repeat = freq[0]
            while repeat > 0:
                result[l] = freq[1]
                result[r] = freq[1]
                r -= 1
                l += 1
                repeat = repeat - 2
        else:
            repeat = freq[0]
            while repeat > 1:
                result[l] = freq[1]
                result[r] = freq[1]
                r -= 1
                l += 1
                repeat = repeat - 2
            key = (repeat, freq[1])
            array_pre.append(key)

    if len(array_pre) >= 1:
        result[l] = array_pre.pop(0)[1]
    print(f"result: {result}")
    return "".join(list(result))



if __name__ == '__main__':
    pairs = [[1, 2], [3, 4], [2, 3]]
    limit = 100
    S = "cbacdcbc"
    string = "444947137"
