import collections
import heapq
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



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

# 1152. Analyze User Website Visit Pattern
def mostVisited(username, timestamp, website):

    table_username = {}
    table_website = {}
    for i in range(len(timestamp)):
        table_username[timestamp[i]] = username[i]
        table_website[timestamp[i]] = website[i]

    timestamp.sort()
    table_lists_byUsers = {}

    for i in range(len(timestamp)):

        keytoSearch = table_username[timestamp[i]]
        if keytoSearch in table_lists_byUsers:
            table_lists_byUsers[keytoSearch].append(table_website[timestamp[i]])
        else:
            table_lists_byUsers[keytoSearch] = [table_website[timestamp[i]]]

    print(table_lists_byUsers)
    freq = {}
    for key in table_lists_byUsers:

        aux = table_lists_byUsers[key]
        visited = set()
        if len(aux) == 3:
            aux_key = (aux[0], aux[1], aux[2])
            if aux_key in freq:
                freq[aux_key] += 1
            else:
                freq[aux_key] = 1
        elif len(aux) > 3:
            tam = len(aux)-2

            for k in range(tam):
                keykey = aux[k]
                for j in range(k+1, len(aux)):
                    arrayAux = list([keykey])
                    arrayAux.append(aux[j])

                    for jj in range(j+1, len(aux)):
                        word = (arrayAux[0],arrayAux[1],aux[jj])

                        if word not in visited:
                            visited.add(word)
                            if word in freq:
                                freq[word] += 1
                            else:
                                freq[word] = 1

    minHeap = []
    for key in freq:
        aux = (-freq[key], key)
        heapq.heappush(minHeap, aux)

    result = heapq.heappop(minHeap)[1]
    return [result[0], result[1], result[2]]

# 49. Group Anagrams
def groupAnagrams(strs):

    ans = {}

    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord("a")] += 1

        tup = tuple(count)
        if tup in ans:
            ans[tup].append(word)
        else:
            ans[tup] = [word]

    result = []
    for key in ans:
        result.append(ans[key])

    return result

# 165. Compare Version Numbers
def compareVersion(version1, version2):
    stringVersion1 = version1.split(".")
    stringVersion2 = version2.split(".")
    firstPartV1 = int(stringVersion1[0])  # first part of String version1
    secondPartV1 = stringVersion1[1:len(stringVersion1)]  # second part of String version2

    firstPartV2 = int(stringVersion2[0])  # second part of String version1
    secondPartV2 = stringVersion2[1:len(stringVersion2)]  # # second part of String version2

    if firstPartV1 < firstPartV2:
        return -1

    if firstPartV1 > firstPartV2:
        return 1

    # we have firstPartV1 == secondPartV2

    V1SumSecondPart = 0
    V2SumSecondPart = 0

    i, j = 0, 0

    while len(secondPartV1) > 0 and len(secondPartV2) > 0:

        num1 = int(secondPartV1.pop(0))
        num2 = int(secondPartV2.pop(0))

        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1

    if len(secondPartV1) == 0 and len(secondPartV2) == 0:
        return 0
    else:
        if len(secondPartV1) != 0:
            suming = 0
            for i in range(len(secondPartV1)):
                suming += int(secondPartV1[i])

            if suming > 0:
                return 1
            else:
                return 0

        else:
            suming = 0
            for i in range(len(secondPartV2)):
                suming += int(secondPartV2[i])

            if suming > 0:
                return -1
            else:
                return 0

# 20. Valid Parentheses
def isValid(cad):

    stack = []
    i = 0
    while i < len(cad):

        if cad[i] == "(" or cad[i] == "[" or cad[i] == "{":
            stack.append(cad[i])
        else:

            if len(stack) <= 0:
                return False

            if cad[i] == ")":
                if stack[len(stack)-1] == '(':
                    stack.pop(len(stack)-1)
                else:
                    return False

            elif cad[i] == "]":
                if stack[len(stack)-1] == "[":
                    stack.pop(len(stack)-1)
                else:
                    return False
            else:
                if stack[len(stack)-1] == "{":
                    stack.pop(len(stack)-1)
                else:
                    return False
        i += 1

    if len(stack) > 0:
        return False
    else:
        return True

# 28. Find the Index of the First Occurrence in a String
def strStr(haystack, needle):

    i, j = 0, 0

    while j < len(haystack):

        aux = j
        while i < len(needle) and aux < len(haystack) and haystack[aux] == needle[i]:
                aux += 1
                i += 1

        if i == len(needle):
            return j
        else:
            i = 0

        j += 1

    return -1

# 2. Add Two Numbers
def addTwonNumbers(l1, l2):

    carry = 0
    result = []
    while l1 != None and l2 != None:

        if l1.val + l2.val + carry >= 10:
            value = (l1.val + l2.val + carry) % 10
            result.append(value)
            l1 = l1.next
            l2 = l2.next
            carry = 1
        else:
            result.append(l1.val + l2.val + carry)
            l1 = l1.next
            l2 = l2.next
            carry = 0

    if l2 != None:
        while l2 != None:

            if l2.val + carry >= 10:
                value = (l2.val + carry) % 10
                result.append(value)
                carry = 1
                l2 = l2.next
            else:
                carry = 0
                result.append(l2.val)
                l2 = l2.next

    if l1 != None:

        while l1 != None:
            if l1.val + carry >= 10:
                value = (l1.val + carry) % 10
                result.append(value)
                carry = 1
                l1 = l1.next
            else:
                result.append(l1.val)
                carry = 0
                l1 = l1.next

    if carry > 0:
        result.append(carry)

    aux = ListNode(result[0])
    ans = aux
    for i in range(1, len(result)):
        aux.next = ListNode(result[i])
        aux = aux.next

    return ans

# 21. Merge Two Sorted Lists
def mergeTwoLists(list1, list2):

    result = []
    res = ListNode()
    aux = res

    while list1 != None and list2 != None:

        if list1.val <= list2.val:
            aux.next = ListNode(list1.val)

            #result.append(list1.val)
            list1 = list1.next
        else:
            #result.append(list2.val)
            aux.next = ListNode(list2.val)
            list2 = list2.next

        aux = aux.next

    while list1 != None:
        aux.next = ListNode(list1.val)
        list1 = list1.next
        aux = aux.next

    while list2 != None:
        aux.next = ListNode(list2.val)
        list2 = list2.next
        aux = aux.next

    while res != None:
        print(res.val)
        res = res.next

    return res

# 206. Reverse Linked List
def reverseList(head):

    prev = None

    while head != None:

        save = head.next
        head.next = prev
        prev = head
        head = save

    return prev

# 25. Reverse Nodes in k-Group { Space Complexity: O(n)}
def reverseKGroup(head, k):

    aux_list = []
    aux_result = []

    while head != None:
        aux_list.append(head.val)
        head = head.next

    i = 0
    while i <= len(aux_list) - 1:

        reverseLocal = []
        if i + k <= len(aux_list):  # can be reversed in the windows i+k
            for j in range(k):
                reverseLocal.insert(0, aux_list[i])
                i += 1
        else:
            for j in range(i, len(aux_list)):
                reverseLocal.append(aux_list[j])
                i += 1

        for jj in range(len(reverseLocal)):
            aux_result.append(reverseLocal[jj])

    aux = ListNode(aux_result[0])
    res = aux

    for kk in range(1, len(aux_result)):
        aux.next = ListNode(aux_result[kk])
        aux = aux.next

    return res

# 7. Reverse Integer
def reverse(x):

    NEG = False
    if x < 0:
        NEG = True
        x = -x

    result = 0
    while x > 0:
        digit = x % 10
        x = x // 10
        print(f"X: {x}")
        if (result > (2**31 -1) // 10):
            return 0
        if (result == (2 ** 31 - 1) // 10 and digit > 7):
            return 0
        result = (result * 10) + digit
        print(f"result: {result}")

    if NEG:
        return -result
    else:
        return result

if __name__ == '__main__':
    word = "-042"
    num = 3200
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    stringArray = ["aba", "abb", "aba"]
    k = 2
    tasks = ["a", "a", "a", "b", "c", "c"]
    nums = [2, 1, 8]
    username = ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"]
    timestamp = [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930]
    website = ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]
    strs = ["eat","tea","tan","ate","nat","bat"]
    version1 = "7.5.2.4"
    version2 = "7.5.3"
    haystack = "mississippi"
    needle = "issipi"
    head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    x = 2147483647
    print(reverse(x))
