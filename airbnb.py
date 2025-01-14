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




if __name__ == '__main__':

    dict = ["ab","cd","yz"]
    print(differByOne(dict))