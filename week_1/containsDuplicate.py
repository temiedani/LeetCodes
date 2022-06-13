from collections import Counter


def containsDuplicate(nums) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if (nums[i] == nums[i+1]):
            return True
    return False


# def containsDuplicate_2(self, nums: List[int]) -> bool:
def containsDuplicate_2(nums) -> bool:
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


def containsDuplicate_3(nums) -> bool:
    x = Counter(nums)
    for i in x.values():
        if i > 1:
            return True
    return False


print(containsDuplicate_2([1, 2, 3, 2, 5]))
