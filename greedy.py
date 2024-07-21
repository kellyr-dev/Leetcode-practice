
# key is to identify when is DP or Greedy
def findboatppl(nums, limit):

    left = 0
    right = len(nums)-1
    nums.sort()

    boat = 0
    while left < len(nums) and left < right:
        if nums[right] + nums[left] <= limit: # be greedy with left
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
    r = len(s)-1

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

    pairs.sort(key=lambda item:item[1])
    maxCount = 1
    j = 1
    i = 0

    while j < len(pairs):
        if pairs[i][1] < pairs[j][0]:
            maxCount += 1
            i = j

        j += 1

    return maxCount

if __name__ == '__main__':

    pairs = [[1,2], [3,4], [2,3]]
                        #[[-7,-1], [0,10], [2,3], [3,6], [3,10], [4,5], [7,9], [7,9]]
                        #[[-7,-1], [2,3], [4,5], [3,6], [7,9], [7,9], [0,10], [3,10]]
    limit = 100
    s = "ebcbbececabbacecbbcbe" #R-> bbececabbacecbb #L-> bececabbacecbbc
    print(findLongestChain(pairs))