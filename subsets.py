
def find_subsets(nums):

    result = [[]]
    if len(nums) == 0:
        return result
    elif len(nums) == 1:
        result.append([nums[0]])
        return result
    elif len(nums) == 2:
        result.append([nums[0]])
        result.append([nums[1]])
        result.append([nums[0], nums[1]])
    else:
        for i in range(len(nums)):
            print(f"result: {result}")
            print(f"i: {i}")
            n = len(result)
            for j in range(n):
                aux = list(result[j])
                print(f"aux: {aux}")
                aux.append(nums[i])
                result.append(aux)


    return result


if __name__ == '__main__':

    nums = [3, 1, 5]
    print(find_subsets(nums))