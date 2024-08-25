
def orderBSearch(nums, key):

    true = False # True -> ascending order | False -> Descending order
    if nums[0] > nums[len(nums)-1]:
        true = False
    else:
        true = True

    def helper(nums, key, left, right):

        middle = int((left + right)/2)

        if key == nums[middle]:
            return middle

        if middle < left or middle > right:
            return -1

        if true:
            if key > nums[middle]:
                return helper(nums, key, middle+1, right)
            else:
                return helper(nums, key, left, middle-1)
        else:
            if key > nums[middle]:
                return helper(nums, key, left, middle-1)
            else:
                return helper(nums, key, middle+1, right)

    result = helper(nums, key, 0, len(nums)-1)
    return result


if __name__ == '__main__':

    nums = [10,9,8,7,6,5,4,3,2,1]
    k = 1
    print(orderBSearch(nums, k))

    # [1, 2, 3, 4, 5, 6, 7]
    # key = 5