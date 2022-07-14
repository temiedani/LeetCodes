if __name__ == "__main__":
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    n = len(a)
    for row in range(n):
        for col in range(n):
            print(a[row][col], end="->")

    print("")
    for col in range(n):
        for row in range(n):
            print(a[row][col], end="->")
