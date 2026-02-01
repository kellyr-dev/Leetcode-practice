import heapq

# 986. Interval List Intersections (no tested)
def intervalIntersection(firstList, secondList):

    prevStart = -1
    prevEnd = -1

    firstStart = 0
    firstEnd = 0
    secondStart = 0
    secondEnd = 0

    i = 0
    j = 0
    result = []

    while i < len(firstList) and j < len(secondList):

        firstStart = firstList[i][0]
        firstEnd = firstList[i][1]

        secondStart = secondList[j][0]
        secondEnd = secondList[j][1]

        print(f"prev: [{prevStart},{prevEnd}]")
        print(f"first: [{firstStart},{firstEnd}]")
        print(f"second: [{secondStart},{secondEnd}]")
        print(f"List: {result}")
        print("<===============================================>")

        # previously check if need to intersecting any of the list with previous interval
        if firstStart <= prevEnd or secondStart <= prevEnd and prevEnd > 0:

            if firstStart <= prevEnd:
                auxStart = min(prevEnd, firstStart)
                auxEnd = min(prevEnd, firstEnd)

                firstStart = max(prevEnd, firstStart)
                firstEnd = max(prevEnd, firstEnd)
                result.append([auxStart, auxEnd])
            else: #if secondStart <= prevEnd and prevEnd > 0:
                auxStart = min(prevEnd, secondStart)
                auxEnd = min(prevEnd, secondEnd)

                secondStart = max(prevEnd, secondStart)
                secondEnd = max(prevEnd, secondEnd)
                result.append([auxStart, auxEnd])

        # intersecting the two list
        if firstStart <= secondEnd:
            if firstEnd <= secondStart:
                #print(f"Here")
                result.append([max(firstStart, secondStart), min(firstEnd, secondEnd)])

        elif secondStart <= firstEnd:
            if secondEnd <= firstStart:
                print(f"Here")
                result.append([max(firstStart, secondStart), min(firstEnd, secondEnd)])

        prevStart = min(firstEnd, secondEnd)
        prevEnd = max(firstEnd, secondEnd)

        i+= 1
        j += 1

    while i < len(firstList):
        if firstStart <= prevEnd:
            auxStart = min(prevEnd, firstStart)
            auxEnd = min(prevEnd, firstEnd)

            firstStart = max(prevEnd, firstStart)
            firstEnd = max(prevEnd, firstEnd)
            result.append([auxStart, auxEnd])

        i += 1

    while j < len(secondList):

        if secondStart <= prevEnd:
            auxStart = min(prevEnd, secondStart)
            auxEnd = min(prevEnd, secondEnd)

            secondStart = max(prevEnd, secondStart)
            secondEnd = max(prevEnd, secondEnd)
            result.append([auxStart, auxEnd])

        j += 1

    return result

# 14. Longest Common Prefix
def longestCommonPrefix(strs):

    if len(strs) == 0:
        return ""

    minHeap = []

    for i in range(len(strs)):
        tam = len(strs[i])
        key = (tam, strs[i])
        minHeap.append(key)

    heapq.heapify(minHeap)
    currentString = heapq.heappop(minHeap)[1]
    i = 0
    result = ""
    while i < len(currentString):
        result += currentString[i]
        flag = True
        for j in range(len(minHeap)): #[]

            aux = minHeap[j][1][0:len(result)]
            if result != aux:
                flag = False

        if flag == False:
            tam = len(result)-1
            if tam > 0:
                return result[0:tam]
            else:
                return "empty"
        i+= 1

    return result


if __name__ == '__main__':
    queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
    firstList = [[14,16]]
    secondList = [[7,13],[16,20]]
    print(intervalIntersection(firstList, secondList))