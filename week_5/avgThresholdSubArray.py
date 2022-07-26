# LeetCode 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
'''
Given an array of integers arr and two integers k and threshold, 
return the number of sub-arrays of size k and average greater than or equal to threshold.

'''


def numOfSubarrays(arr, k, threshold):
    """
    :type arr: List[int]
    :type k: int
    :type threshold: int
    :rtype: int
    """
    windowStart = 0
    windowEnd = k-1
    count = 0
    runningSum = sum(arr[windowStart:windowEnd])
    while windowEnd < len(arr):
        runningSum += arr[windowEnd]
        if (runningSum/k) >= threshold:
            count += 1
        runningSum -= arr[windowStart]
        windowStart += 1
        windowEnd += 1
    return print(count)


if __name__ == "__main__":
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    numOfSubarrays(arr, k, threshold)
    # Output: 3
    '''
    Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. 
    All other sub-arrays of size 3 have averages less than 4 (the threshold).
    '''
