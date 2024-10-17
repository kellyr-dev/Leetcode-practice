
# 1991. Find the Middle Index in Array
def findMiddleIndex(nums):

    idxLeftMost = -1

    prefix = [0] * len(nums)
    prefix[0] = nums[0]

    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] + nums[i]

    limit = len(prefix)-1
    print(prefix)
    sumLeft = 0
    for j in range(len(prefix)):

        if j == 0:
            sumLeft = 0
        else:
            sumLeft = prefix[j-1]

        sumRight = prefix[len(prefix) - 1] - prefix[j]

        print(f"sumRight: {sumRight} -> j:{j}")

        if sumLeft == sumRight:
            idxLeftMost = j

    return idxLeftMost

# 2574. Left and Right Sum Differences
def leftRightDifference(nums):

    resulDiff = [0] * len(nums)
    prefix = [0] * len(nums)

    prefix[0] = nums[0]
    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] + nums[i]

    sumLeft = 0
    sumAll = prefix[len(prefix)-1]
    for j in range(len(prefix)):

        if j >= 1:
            sumLeft = prefix[j-1]

        sumRight = sumAll - prefix[j]

        diff = abs(sumLeft - sumRight)
        resulDiff[j] = diff

    return resulDiff


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5]
    print(leftRightDifference(nums1))