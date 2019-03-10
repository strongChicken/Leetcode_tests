def searchInsert(nums:list, target:int):
    L_List = 0
    R_List = len(nums)

    while(L_List > R_List):
        mid = (R_List - L_List) // 2
        if target > nums[mid]:
            L_List = mid

        elif target < nums[mid]:
            R_List = mid
        else:
            return  mid


test = [1,2,3,4]
T = 3
print(searchInsert(test,T))
