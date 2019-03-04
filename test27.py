def removeElement(self, nums: List[int], val: int) -> int:
    if len(nums) == 0:
        return 0

    _s = 0

    for f in range(0,len(nums)):    # f 一直遍历整个List，
        if nums[f] != val:          # 当nums[f] == val时，f指针跳过 当前元素，继续遍历。直到找到一个不等于val的元素的位置（new)f
            nums[_s] = nums[f]      # 将不等于val的元素赋值给 _s 位置的元素，只要 f 位置的元素不等于 val，就会持续赋值。——
            _s += 1                 # ——即使后续有连续元素 等于 val，但持续的赋值会保持 （!=val）的元素连续覆盖。
                                    # _s += 1保证了指针有序的遍历，f指针把合适的元素赋值（覆盖）_s 位置的元素

    return _s


