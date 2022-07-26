def slidingWindow(nums: list) -> int:
    maxSum = currentSum = 0
    # start = end = 0
    # while end<len(nums):
    #     currentSum=
    #     maxSum=max(maxSum, currentSum)
    #     end+=1:
    return print(maxSum)

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    largest_sum=float("-inf")
    current_sum=nums[0]
    start=0
    end=1
    while end<len(nums):
        current_sum+=nums[end]
        if nums[start]<0:
            current_sum-=nums[start]
            start+=1
        largest_sum=max(largest_sum,current_sum)
        end+=1
        
    return largest_sum


if __name__ == "__main__":
    # nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    # slidingWindow(nums)
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))
