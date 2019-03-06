def strStr(haystack: str,needle: str):
    ND_Point = 0

    same = 0
    diff = 0

    for Hs_Point in range(len(haystack)):
        if haystack[Hs_Point] == needle[ND_Point]:  #如何处理ND_Point的边界问题
            ND_Point += 1                           #当needle已经遍历完，haystack还没有遍历完
            same += 1
        else:
            ND_Point == 0
            diff += 1
    return ND_Point

print(strStr("hello", "ll"))

