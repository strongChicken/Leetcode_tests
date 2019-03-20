def lengthOfLastWord(s:str):
    stack = []
    l_word = 0
    l_str = len(s)

    for i in range(l_str):
        element = s[i]
        if element != ' ':
            l_word += 1
            print("l_word1: ", l_word, "i: ", i)
        if (element == ' ' and l_word != 0) or (i == (l_str - 1) and l_word != 0):
            stack.append(l_word)
            print("l_word2: ", l_word)
            l_word = 0

    print(stack)
    print("l_str", l_str)
    return stack[-1]

test = ' hello world mr   '
print(lengthOfLastWord(test))

