# 2099. Find Subsequence of Length K With the Largest Sum
'''
You are given an integer array nums and an integer k. 
You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some 
or no elements without changing the order of the remaining elements.

'''


def maxSubsequence(nums, k):
    if k == 1:
        return max(nums)
    current_sum = nums[0]+nums[1]
    for num in nums[1:]:
        current_sum = max(current_sum, current_sum+num)
    return print(current_sum)


maxSubsequence([7, 1, 2, -1, 3, 4, 10, -12, 3, 21, -19])


@1Hiwetey
