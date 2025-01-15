# 1554. Strings Differ by One Character
def differByOne(dict):

    for i in range(len(dict)): # O(n)

        word = dict[i]
        for j in range(i+1, len(dict)):
            auxWord = dict[j]
            count = 0
            for k in range(len(auxWord)):
                if word[k] != auxWord[k]:
                    count += 1

                if count >= 2:
                    break

            if count == 1 and len(word) > 1:
                return True

    return False

# 136. Single Number
def singleNumber(nums):

    num = 0
    for value in nums:

        print(f"num: {num} XOR value: {value}")
        num = num ^ value
        print(f"resutl: {num}")

    return num

if __name__ == '__main__':

    #nums = [1,1,2,2,4]
    nums = [4,1,2,1,2]
    print(singleNumber(nums))