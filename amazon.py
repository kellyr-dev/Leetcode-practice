import heapq
from collections import Counter

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
    end = len(nums) - 1
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
    index = len(string) - 1
    result = []
    i = 0

    while index >= 0:
        i += 1
        digit = int(string[index])
        if i == 1:
            if digit != 0:
                result.append(hash_table[digit])
        if i == 2:  # decenas
            new_digit = digit

            if new_digit >= 1 and new_digit <= 3:
                result_aux = ""
                for j in range(new_digit):
                    result_aux += "X"
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

        if i == 3:  # centenas
            new_digit = digit
            if new_digit >= 1 and new_digit <= 3:
                result_aux = ""
                for j in range(new_digit):
                    result_aux += "C"
                result.insert(0, result_aux)

            elif new_digit == 4:
                result.insert(0, "CD")

            elif new_digit >= 5 and new_digit <= 8:
                result_aux = "D"
                for j in range(5, new_digit):
                    result_aux += "C"
                result.insert(0, result_aux)

            elif new_digit == 9:  # DCCC # LM
                result.insert(0, "CM")

        if i == 4:  # milesas
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

        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,

    }

    if len(string) == 1:
        return hash_table[string]

    current = len(string) - 2
    prev = len(string) - 1
    result = hash_table[string[prev]]

    while current >= 0:
        if hash_table[string[current]] < hash_table[string[prev]]:
            result -= hash_table[string[current]]
        else:
            result += hash_table[string[current]]

        current -= 1
        prev -= 1

    return result

# 819. Most Common Word
def mostCommonWord(paragraph, banned):
    new_string = paragraph.lower().rstrip()

    table_banned = set()

    othersChars = [",", ";", "!", "?", "."]
    others = set(othersChars)

    for i in range(len(banned)):
        table_banned.add(banned[i])

    freq = {}
    word = ""
    for j in range(len(new_string)):
        if new_string[j] == " " or new_string[j] in others:
            if word != " " and len(word) > 0:
                if word in freq:
                    freq[word] += 1
                    word = ""
                else:
                    freq[word] = 1
                    word = ""
        else:
            word += new_string[j]

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

    maxHeap = []

    for key in freq:
        if key not in table_banned:
            value = freq[key]
            keyAux = (-value, key)
            heapq.heappush(maxHeap, keyAux)

    result = heapq.heappop(maxHeap)[1]
    return result

# 937. Reorder Data in Log Files
def reorderLogFiles(logs):
    digits = []  # queue for storing relative order that appears in the log file
    minHeap = []  # Heap ordered log by (key1, key2) where key1 is content and key2 is id

    for i in range(len(logs)):  # O(n)

        log = logs[i].split(" ")
        print(f"log: {log}")
        all_digit = 0
        all_letter = 0
        content = ""
        id = log[0]
        for j in range(1, len(log)):  # O(k) k is words (space separate) in a log

            if log[j].isnumeric():
                all_digit += 1
            else:
                all_letter += 1

            content = content + log[j] + " "

        if all_letter == 0:
            digits.append(logs[i])
        else:
            key = (content, log[0])
            heapq.heappush(minHeap, key)

    result = []
    print(f"minHeap: {minHeap}")
    while len(minHeap) > 0:
        aux = heapq.heappop(minHeap)
        aux_log = aux[1] + " " + aux[0]
        result.append(aux_log.rstrip())

    while len(digits) > 0:
        result.append(digits.pop(0))
    return result

# 42. Trapping Rain Water
def trap(height):
    left_max = 0
    right_max = 0
    left = [0] * len(height)
    right = [0] * len(height)
    trapped = [0] * len(height)

    for i in range(len(height)):
        left[i] = left_max
        left_max = max(left_max, height[i])

    for j in range(len(height) - 1, 0, -1):
        right[j] = right_max
        right_max = max(right_max, height[j])

    for i in range(len(height)):
        trapp = min(left[i], right[i]) - height[i]
        if trapp > 0:
            trapped[i] = trapp



if __name__ == '__main__':
    word = "-042"
    num = 3200
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    stringArray = ["aba", "abb", "aba"]
    k = 2
    tasks = ["a", "a", "a", "b", "c", "c"]
    nums = [2, 1, 8]
    print(trap(nums))
