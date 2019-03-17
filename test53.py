def maxSubArray(nums):
    nums_L = len(nums)
    tempcount = maxcount = nums[0]

    if nums_L == 1:
        return nums[0]
    elif nums_L == 2:
        maxcount = nums[0] + nums[1]
        if nums[0] > maxcount:
            maxcount = nums[0]
            # print("step1 max：", maxcount)
        if nums[1] > maxcount:
            maxcount = nums[1]
            # print("step2 max：",maxcount)
        return maxcount

    for i in range(nums_L):
        tempcount = nums[i]
        for j in range(i+1,nums_L):
            print("max: ",maxcount,"temp: ",tempcount, "i: ",i, "j: ",j)
            if tempcount > maxcount:
                tempcount += nums[j]
                maxcount = tempcount


    return maxcount


testlist = [-2,-1,-3,-1]
print(maxSubArray(testlist))
print("sum: ",sum(testlist))