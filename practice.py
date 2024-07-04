
def lengOfLastWord(word):

    right = len(word)-1
    cont = 0
    found = True
    while right >0:
        if word[right] == " ":
            if cont > 0:
                cont += 1
                right -= 1
            else:
                return cont
        else:
            cont += 1
            right -=1


    print(word)
    print(cont)

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    word = "Hello World"
    print(lengOfLastWord(word))