# Time Complexity -O(n)
# Space Cpmplexity-O(n)
def solution(matrix):
    # Final result accumulator
    result = []
    # Helper Function to find Border sum

    def borderSum(bordermatrix):
        n = len(bordermatrix)
        sums = 0
        # Base Case is n=2
        # loop over border elements
        for i in range(0, n):
            for j in range(0, n):
                # check if border element
                if (i == 0 or j == 0 or i == n - 1 or j == n - 1):
                    sums = sums + bordermatrix[i][j]
        # print("\nSum of boundary is", sums)
        return sums
    result.append(borderSum(matrix))
    n = len(matrix)
    m = len(matrix)-2
    while m >= 2:
        innerMatrix = [[0]*m]*m
        for i in range(len(innerMatrix)):
            innerMatrix[i] = matrix[i+1][n-m-1:n-1]
        m -= 2
        # Recursively call the function on the inner Matrix
        result.append(borderSum(innerMatrix))
    # return the final result
    return print(result)

# Main Function to test the code
# if __name__=="main":
matrix2 = [[1, 2], [1, 2]]
matrix4 = [[1,  2,  2,  3],
        [0,  1,  0,  2],
        [4, -1, -1, -3],
        [4, -1, -1,  3]]
matrix6 = [[1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]]
matrix8 = [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]

solution(matrix2)
solution(matrix4)
solution(matrix6)
solution(matrix8)