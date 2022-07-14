def solution(nums, queries):
    sum = 0
    for i in range(len(queries)):
        x = 0
        for j in range(queries[i][0], queries[i][1]+1):
            x += nums[j]
        print(x)
    return sum


if __name__ == "__main__":
    nums = [3, 0, -2, 6, -3, 2]
    queries = [[0, 2], [2, 5], [0, 5]]
    print(solution(nums, queries))
