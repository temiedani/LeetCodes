def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    anchor = length = 0
    for i in range(len(nums)):
        if i > 0 and nums[i-1] >= nums[i]:
            anchor = i
        length = max(length, i-anchor+1)
    return length


if __name__ == "__main__":
    x = [10, 9, 2, 5, 3, 7, 101, 18]
    # y = [0, 1, 0, 3, 2, 3]
    # z = [7, 7, 7, 7, 7, 7, 7]

    print(lengthOfLIS(x))
    xx = [5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]
    print(sum(xx))
