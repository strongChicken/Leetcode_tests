# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

def strStr(haystack: str,needle: str):
    if (haystack == "") or (needle == ""):
        return 0

    HS_L = len(haystack)
    ND_L = len(needle)

    ND_Point = 0
    HS_Point = 0

    while((HS_Point < HS_L) and (ND_Point < ND_L)):
        if haystack[HS_Point] != needle[ND_Point]:
            HS_Point = HS_Point - ND_Point + 1  # 用HS指针位置 - ND指针位置 会得到 HS原指针位置，事实上需要在HS[原位置+1]的位置开始继续配对
            ND_Point = 0
        else:
            HS_Point += 1
            ND_Point += 1


    if ND_Point == ND_L:
        return HS_Point - ND_Point  # 返回needle 出现的第一个位置
    else:
        return -1

print(strStr("", "a"))

