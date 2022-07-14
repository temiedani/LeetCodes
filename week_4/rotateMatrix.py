def rotateMatrix(a):
    n = len(a)
    # transpose of matrix swap row and matrix
    for i in range(n):
        for j in range(i):
            if i != j:
                a[i][j], a[j][i] = a[j][i], a[i][j]

    # reverse each row
    for i in range(n):
        a[i].reverse()
    return a


if __name__ == "__main__":
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print(rotateMatrix(a))
    ''' Program to transpose a matrix using list comprehension'''

    X = [[12, 7],
         [4, 5],
         [3, 8]]

    result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

    for r in result:
        print(r)

        # Program to transpose a matrix using a nested loop

    X = [[12, 7],
         [4, 5],
         [3, 8]]

    result = [[0, 0, 0],
              [0, 0, 0]]

    # iterate through rows
    for i in range(len(X)):
        # iterate through columns
        for j in range(len(X[0])):
            result[j][i] = X[i][j]
