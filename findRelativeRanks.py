# 506. Relative Ranks
'''
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. 
All the scores are guaranteed to be unique.

The athletes are placed based on their scores, 
where the 1st place athlete has the highest score, 
the 2nd place athlete has the 2nd highest score, and so on. 
The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, 
their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

'''
import heapq

# Solution1: Using max Heap


def findRelativeRanks(score):
    res = {}
    rank = 1
    max_heap = [-s for s in score]
    heapq.heapify(max_heap)
    while len(max_heap) > 0:

        s = heapq.heappop(max_heap)
        if rank == 1:
            res["Gold Medal"] = score.index(-s)
        elif rank == 2:
            res["Silver Medal"] = score.index(-s)
        elif rank == 3:
            res["Bronze Medal"] = score.index(-s)
        else:
            res[str(rank)] = score.index(-s)
        rank += 1

    # sort by index
    output = sorted(res, key=lambda x: res[x])
    return output

# Solution 2: Using list indices


def findRelativeRanks_2(score):
    indicies = {v: idx for idx, v in enumerate(score)}
    result = [0 for _ in score]
    ranks = {0: 'Gold Medal', 1: 'Silver Medal', 2: 'Bronze Medal'}

    for i, v in enumerate(sorted(score)[::-1]):
        index = indicies[v]
        result[index] = ranks[i] if i in range(3) else str(i + 1)

    return print(result)


if __name__ == '__main__':

    score = [5, 4, 3, 11, 2, 1, 77]
    indicies = {idx: val for idx, val in enumerate(score)}
    # Sorting a Dictionary
    # print(sorted(indicies, key=lambda x: indicies[x], reverse=True))

    print(findRelativeRanks(score))
    findRelativeRanks_2(score)
