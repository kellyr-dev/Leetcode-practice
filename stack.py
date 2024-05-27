import re

# 20. Valid Parentheses
def isValid(str):
    stack_of = []

    for i in range(len(str)):

        if str[i] == "(" or str[i] == "[" or str[i] == "{":
            stack_of.append(str[i])

        else:
            if len(stack_of) == 0:
                return False
            else:
                top = len(stack_of) - 1

                if str[i] == ")" and stack_of[-1] == "(" or str[i] == "]" and stack_of[-1] == "[" or str[i] == "}" and \
                        stack_of[-1] == "{":
                    stack_of.pop(-1)
                else:
                    return False

    if len(stack_of) == 0:
        return True
    else:
        return False

# 71. Simplify Path
def simplifyPath(text):
    if text[0] != "/":
        return "/"

    left = 0
    right = 1
    stacks_of = []

    pattern = re.compile('[A-Za-z]') # pattern only characters

    while right < len(text):

        if text[right] == "/":
            if right - left > 1:

                aux = text[left:right]
                aux_toput = text[left + 1:right] # inclusive left range # exclusive right range

                if re.search(pattern, aux_toput) or aux_toput == "...":  # if is only letters
                    stacks_of.append(aux)
                    left = right

                elif aux_toput == "..":  # if /../ pop directory from stack
                    if stacks_of:
                        stacks_of.pop(len(stacks_of) - 1)
                        left = right
                    else:
                        left = right
                elif aux_toput == ".":
                    left = right
            else:
                left += 1
        right += 1

    if (right - left) > 1:
        last_word_toput = text[left + 1:right]
        last_word = text[left:right]
        if re.search(pattern, last_word_toput) or last_word_toput == "...":
            stacks_of.append(last_word)

        elif last_word_toput == "..":
            if stacks_of:
                stacks_of.pop(len(stacks_of) - 1)

    print(stacks_of)

    if len(stacks_of) > 0:
        return "".join(list(stacks_of))
    else:
        return "/"

# 71. Simplify Path
def simplifyPathAlter(text):

    splitted = text.split("/") # O(log(n))
    stacks_of = []
    pattern = re.compile('[A-Za-z]')

    for word in splitted:

        if word == "...":
            stacks_of.append(word)
        elif word == "..":
            if stacks_of:
                stacks_of.pop(len(stacks_of)-1)
        elif word == "." or word == "/" or word == "":
            continue
        else:
            stacks_of.append(word)

    if len(stacks_of) == 0:
        return "/"
    else:
        aux = "/".join(list(stacks_of))
        print(aux)
        return aux

# 1249. Minimum Remove to Make Valid Parentheses
def minRemoveToMakeValid(s):

    string = list(s)
    stck = []
    for i in range(len(string)):
        if stck:
            print(f"i:{i} -> {stck}")

        if string[i] == '(':
            stck.append(i)

        elif string[i] == ')':
            if len(stck) > 0:
                stck.pop()
            else:
                string[i] = ''

    while stck:
        string[stck.pop()] = ''

    return ''.join(string)


if __name__ == '__main__':
    string = "))(("
    num = [13, 7, 6, 12]
    print(minRemoveToMakeValid(string))
