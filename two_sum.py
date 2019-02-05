def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    D = {}
    for index, value in enumerate(nums):
        if D.get(target - value) is not None:
            return [D.get(target - value), index]
        else:
            D[target - value] = index
    
    return None

print(twoSum([2, 7, 11, 15], 9))
