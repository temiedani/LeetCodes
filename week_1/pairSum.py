from collections import defaultdict


def pairSum(nums, sum):
    visited = set()
    res = set()
    for i in nums:
        target = sum-i
        # is target
        if target not in visited:
            visited.add(target)
        else:
            res.add(nums, target)
    return


print(pairSum([1, 2, 3, 2, 0, 4, 5], 5))
