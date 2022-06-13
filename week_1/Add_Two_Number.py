class Solution:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def addTwoNumbers(self):
        sum1 = 0
        sum2 = 0
        for i in range(len(self.l1)):
            sum1 += self.l1[i]*(10**i)
        for j in range(len(self.l2)):
            sum2 += self.l2[j]*(10**j)
        sum = sum1+sum2
        x = str(sum)[::-1]
        result = []
        for i in range(len(x)):
            result.append(int(x[i]))
        return (result)


l1 = [2, 4, 3]
l2 = [5, 6, 4]
p1 = Solution(l1, l2)
print(p1.addTwoNumbers())
l1 = [9, 9, 9, 9, 9, ]
l2 = [9, 9, 9, 9]
p1 = Solution(l1, l2)
print(p1.addTwoNumbers())
