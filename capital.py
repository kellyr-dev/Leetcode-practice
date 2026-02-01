
# 3161. Block Placement Queries (TLE)
def getResultsTLE(queries):

    minRange = 0
    maxRange = float('-inf')
    result = []

    for query in queries:
        maxRange = max(maxRange, query[1])

    interval = [[0,maxRange]]
    timeline = [0] * (maxRange + 1)

    for query in queries:
        type = query[0]
        if type == 1:
            wall = query[1]
            for i in range(len(interval)):
                rang = interval[i]
                if wall > rang[0] and wall <= rang[1]:
                    newRang = [rang[0], wall]
                    interval[i] = [wall, rang[1]]
                    interval.append(newRang)
                    break
        else:
            size = query[2]
            limit = query[1]

            if size > limit:
                result.append(False)
            else:
                tam = len(result)
                result.append(False)
                for rang in interval:
                    if rang[1] - rang[0] >= size: # if room for the size in X interval
                        if rang[0] < limit: # if overlaping the interval
                            newRang1 = min(rang[1], limit) # recalculate right limit and size
                            if newRang1 - rang[0] >= size:
                                result[tam] = True
                                break

    print(interval)
    # Summarizing
    # for each query = wall update the intervals
    # for each query = placing check if there is intervals with room for the placing
    # if there is at least one interval with room for placing recalculate limits based on right_limit of the placing
    # recalculate limits is basically check the overlaping requirements
    # if still there is a room for the placing put True in the array for result
    # if not a room put False
    return result



if __name__ == '__main__':
    queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
    board = [[110,5,112,113,114],
             [210,211,5,213,214],
             [310,311,3,313,314],
             [410,411,412,5,414],
             [5,1,512,3,3],
             [610,4,1,613,614],
             [710,1,2,713,714],
             [810,1,2,1,1],
             [1,1,2,2,2],
             [4,1,4,4,1014]]

    print(getResultsTLE(queries))

