
# 3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(word):

    maxLenght = 0
    table_set = set()
    left = 0
    right = 0

    while right < len(word):

        if word[right] not in table_set:
            table_set.add(word[right])
            maxLenght = max(maxLenght, right - left + 1)

        else:
            while word[right] in table_set:
                table_set.remove(word[left])
                left += 1

            table_set.add(word[right])

        right += 1

    return maxLenght

# 8. String to Integer (atoi)
def myAtoi(s):

    NEG = False  # For checking if first num is -
    DIGIT = False  # For checking if a first element is already a digit Not Zero
    start = 0
    string = s.strip()
    MINIMUM = -2147483648
    MAXMUM = 2147483647

    if len(string) == 0:
        return 0

    final_string = ""

    if string[0] == "-":
        NEG = True
        start = 1

    if string[0] == "+":
        start = 1

    while start < len(string):
        if string[start].isnumeric() and string[start] != "0":
            DIGIT = True
            final_string += string[start]

        elif string[start].isnumeric() and string[start] == "0":
            if DIGIT == True:
                final_string += string[start]

        else:
            break

        start += 1

    # need to check if -0asd or +0asd
    # if no Python declare a var long and compare if you result is greater than or less than

    if len(final_string) == 0:
        return 0

    result = int(final_string)

    if NEG:
        result = -result

    if result >= MINIMUM and result <= MAXMUM:
        return result
    elif result > MAXMUM:
        return MAXMUM
    else:
        return MINIMUM

# 11. Container With Most Water
def maxArea(nums):

    maxContainer = 0
    end = len(nums)-1
    start = 0

    while start < end:
        area = (end - start) * min(nums[start], nums[end])
        maxContainer = max(maxContainer, area)

        if nums[start] <= nums[end]:
            start += 1
        else:
            end -= 1

    return maxContainer



if __name__ == '__main__':

    word = "-042"
    nums = [1,8,6,2,5,4,8,3,7]
    print(maxArea(nums))