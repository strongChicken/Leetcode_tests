def lengthOfLastWord(s:str):
    stack = []
    l_word = 0
    l_str = len(s)


    for i in range(l_str):
        element = s[i]
        if element != ' ':
            l_word += 1
            print("l_word1: ", l_word, "i: ", i)
        if (element == ' ' and l_word != 0) or (i == (l_str - 1) and l_word != 0):  # 当元素为space时，而且l_word已经记录了单词长度时，则压入栈；当到了最后一个元素时，也是同样的方式；
            stack.append(l_word)                                                    # 该方式是避免最后边界是space，导致……（忘了）
            print("l_word2: ", l_word)
            l_word = 0

    if len(stack) == 0:
        return 0

    print(stack)
    print("l_str", l_str)
    return stack[-1]

test = '  '
print(lengthOfLastWord(test))

print(len(test))

