# LeetCode 35. Search Insert Position
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

# Linear Solution


def searchInsert(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: int
    """
    position = 0
    # target at begining of array
    if target < nums[0]:
        return 0
    # target at the end of array
    if target > nums[-1]:
        return len(nums)

    for i, v in enumerate(nums):
        if v == target:
            return i
        if target > v:
            position += 1
    return position

# logarithmic Solution


def searchInsert_2(nums, target):
    start = 0
    end = len(nums)-1

    while(start <= end):
        middle = (start+end)//2
        if nums[middle] == target:
            return middle
        # target is on the right side
        elif nums[middle] < target:
            start = middle+1
        # target is on the left side
        else:
            end = middle-1

    return start
