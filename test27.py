def removeElement(self, nums: List[int], val: int) -> int:
    if len(nums) <= 1 and nums[0] != val:
        return len(nums)

    _s = 0

    if nums[0] != val:
        for i in range(1, len(nums)):
