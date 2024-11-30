
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

# 12. Integer to Roman
def intORoman(num):

    hash_table = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }

    if num < 0 or num >= 4000:
        return ""

    string = str(num)
    index = len(string)-1
    result = []
    i = 0

    while index >= 0:
        i += 1
        digit = int(string[index])
        if i == 1:
            if digit != 0:
                result.append(hash_table[digit])
        if i == 2: # decenas
            new_digit = digit

            if new_digit >= 1 and new_digit <= 3:
                result_aux = ""
                for j in range(new_digit):
                    result_aux+= "X"
                result.insert(0, result_aux)

            elif new_digit == 4:
                result.insert(0, "XL")

            elif new_digit >= 5 and new_digit <= 8:
                result_aux = "L"
                for j in range(5, new_digit):
                    result_aux += "X"
                result.insert(0, result_aux)

            elif new_digit == 9:
                result.insert(0, "XC")

        if i == 3: # centenas
            new_digit = digit
            if new_digit >= 1 and new_digit <= 3:
                result_aux = ""
                for j in range(new_digit):
                    result_aux+= "C"
                result.insert(0, result_aux)

            elif new_digit == 4:
                result.insert(0, "CD")

            elif new_digit >= 5 and new_digit <= 8:
                result_aux = "D"
                for j in range(5, new_digit):
                    result_aux += "C"
                result.insert(0, result_aux)

            elif new_digit == 9: # DCCC # LM
                result.insert(0, "CM")

        if i == 4: # milesas
            new_digit = digit
            if new_digit >= 1 and new_digit <= 3:
                result_aux = ""
                for j in range(new_digit):
                    result_aux += "M"
                result.insert(0, result_aux)

        index -= 1

    return "".join(list(result))

# 13. Roman to Integer
def romanToInt(string):

    hash_table = {

        "I" : 1,
        "II" : 2,
        "III" : 3,
        "IV" : 4,
        "V" : 5,
        "VI" : 6,
        "VII" : 7,
        "VIII" : 8,
        "IX" : 9,
        "X" : 10,
        "XL" : 40,
        "L": 50,
        "C" :100,
        "D" : 500,
        "M" : 1000,

    }

    if len(string) == 1:
        return hash_table[string]

    current = len(string)-2
    prev = len(string)-1
    result = hash_table[string[prev]]

    while current >= 0:
        if hash_table[string[current]] < hash_table[string[prev]]:
            result -= hash_table[string[current]]
        else:
            result += hash_table[string[current]]

        current -= 1
        prev -= 1

    return result


if __name__ == '__main__':

    word = "-042"
    nums = [1,8,6,2,5,4,8,3,7]
    num = 3200
    string = "LVIII"
    print(romanToInt(string))