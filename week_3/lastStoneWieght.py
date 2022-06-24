# 1046. Last Stone Weight
'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. 
On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y. 
The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, 
and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. 
If there are no stones left, return 0
'''
import heapq


class Solution(object):
    # Max heap solution O(log(n))
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first < second:
                heapq.heappush(stones, first-second)
        stones.append(0)
        return abs(stones[0])
    # Recursive solution

    def lastStoneWeight_2(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        if len(stones) == 1:
            return stones[0]
        if len(stones) == 0:
            return 0

        stones.sort()

        if stones[-2] == stones[-1]:
            return self.lastStoneWeight_2(stones[:-2])
        else:
            stones[-1] = stones[-1] - stones[-2]
            del stones[-2]
            return self.lastStoneWeight_2(stones)
