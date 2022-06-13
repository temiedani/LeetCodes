
from collections import Counter
# Bucket sort


def topKFrequent(nums, k):
    if len(nums) == k:
        return nums
    x = Counter(nums)
    return [i[0] for i in x.most_common(k)]


def topKFrequent_2(nums, k: int):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

        # O(n)


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 11,
            11, 11, 11, 11, 11, 11, 11, 3, 7, 7, 7, 7]
    k = 2


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 11,
            11, 11, 11, 11, 11, 11, 11, 3, 7, 7, 7, 7]
    k = 2
    print(topKFrequent(nums, k))
    print(topKFrequent_2(nums, k))
    count = {}
    for i in nums:
        count[i] = 1+count.get(i, 0)
    print(count)
