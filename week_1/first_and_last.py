def first_and_last(nums, target: int):
    index = []
    for i in range(len(nums)):
        if(nums[i] == target):
            index.append(i)
    if(len(index) == 0):
        return [-1, -1]
    return [min(index), max(index)]

#  T-O(n) S-O(n)


def searchRange(nums, target):
    outList = [-1, -1]
    for i in range(len(nums)):
        if nums[i] == target and outList[0] == -1:
            outList[0] = i
        elif nums[i] == target and outList[0] != -1:
            outList[1] = i
    if outList[0] != -1 and outList[1] == -1:
        outList[1] = outList[0]
    return outList

# better solution with binary search
