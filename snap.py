import heapq

# 151. Reverse Words in a String
def reverseWords(s):

    auxWords = s.split(" ")
    print(auxWords)
    resultWords = []
    for word in auxWords:

        current = word.strip()
        print(f"current: {current}")
        if current != "" and current != " ":
            resultWords.insert(0, current)

    return " ".join(list(resultWords))


if __name__ == '__main__':

    words = ["like","god","internal","me","internet","interval","intension","face","intrusion"]
    s = "the sky is blue"
    print(reverseWords(s))