def maxSubArray(nums):
    nums_L = len(nums)
    maxcount = nums[0]
    tempcount = 0

    for i in range(nums_L):
        tempcount += nums[i]    # tempcount 可以看作一枚指针，指针位置的元素相加小于0，代表往后相加只会造成更小的值，而不是使 总和 变大。这是核心思想。
        if tempcount > maxcount:
            maxcount = tempcount
        if tempcount < 0:
            tempcount = 0       # 当tempcount < 0 时，即"和"不具备增值效益，继续相加，只会减少总和，故舍去
                                # 为什么没有 tempcount = maxcount 的判断，因为没有意义，当两个值相同，意味着就看下一个位置的元素是否为负数，继续循环判断。
    return maxcount


testlist = [-1,4]
print(maxSubArray(testlist))
print("sum: ",sum(testlist))