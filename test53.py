def maxSubArray(nums):
    nums_L = len(nums)
    tempcount = maxcount = nums[0]

    for i in range(nums_L):
        tempcount = nums[i]
        for j in range(i+1,nums_L):
            tempcount += nums[j]
            print("max: ",maxcount,"temp: ",tempcount, "i: ",i, "j: ",j)
            if tempcount > maxcount:
                maxcount = tempcount


    return maxcount


testlist = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(testlist))
print("sum: ",sum(testlist))