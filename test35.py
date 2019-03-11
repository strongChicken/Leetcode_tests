def searchInsert(nums:list, target:int):
    L_List = 0
    R_List = len(nums) - 1

    while(L_List <= R_List):
        mid = (R_List + L_List) // 2
        if target > nums[mid]:
            L_List = mid + 1
        elif target < nums[mid]:
            R_List = mid - 1
        elif target == nums[mid]:
            return mid

    # return L_List         # 为什么返回左边界？

test = [1,3,4,5,7]
T = 8

print(searchInsert(test,T))
