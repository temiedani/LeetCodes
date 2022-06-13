def isPalindrome(x):
    word = str(x)
    rev = word[::-1]
    return word == rev


testCases = [121, -121, 10, 101]
for i in testCases:
    print(isPalindrome(i), end="\t")
