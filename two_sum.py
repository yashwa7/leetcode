# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]. go

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
