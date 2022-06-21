# 1464. Maximum Product of Two Elements in an Array

'''
Given the array of integers nums, 
you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).
'''
import heapq


class Solution(object):
    # Using maxheap
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [-s for s in nums]
        heapq.heapify(nums)
        first = -(heapq.heappop(nums))
        second = -(heapq.heappop(nums))
        return (first-1)*(second-1)


class Solution_2(object):
    # Using max function
    def maxProduct_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n1 = max(nums)
        nums.pop(nums.index(n1))
        n2 = max(nums)
        return (n1-1)*(n2-1)
