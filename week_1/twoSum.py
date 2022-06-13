def twoSum(nums, target: int):
    # given exactly atleast one solution
    output = []
    if(len(nums) == 2):
        return [0, 1]
    visited = {}
    for index, value in enumerate(nums):
        diff = target-value
        if diff in visited:
            output.append([visited[diff], index])
            # return(visited[diff], index)
        visited[value] = index
    return output


print(twoSum([1, 2, 3, 4, 3, 5], 6))
