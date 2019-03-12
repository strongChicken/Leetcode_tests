def searchInsert(nums:list, target:int):
    L_List = 0
    R_List = len(nums) - 1

    if nums == None:
        return None

    while(L_List <= R_List):
        mid = (R_List + L_List) // 2
        if target > nums[mid]:
            L_List = mid + 1
        elif target < nums[mid]:
            R_List = mid - 1
        elif target == nums[mid]:
            return mid

    return L_List         # 为什么返回左边界？ 通过<实例>，无论是超出左边界还是右边界，或者是不存在的数的坐标，都是等于左边界。

