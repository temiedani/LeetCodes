def printPat(n):
    temp = n
    s = ""
    while (temp >= 1):
        for i in range(n):
            p = str(n-i) + " "
            if temp == 0:
                break
            s += temp * p
        s += "$"
        temp -= 1
    return s


print(printPat(3))
