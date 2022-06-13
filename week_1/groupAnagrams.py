
from collections import Counter, defaultdict
from itertools import count


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    output = []
    for index, word in enumerate(strs):
        x = []
        temp = index
        while((Counter(strs[index]) == Counter(strs[temp])) and (temp < len(strs))):
            x.append(strs[temp])
            temp += 1
        output.append(x)
    return output


def groupAnagrams_2(strs):
    result = {}
    output = []
    for i in strs:
        result[i] = Counter(i)
    # for index, word in enumerate(strs):
    #     if Counteword) in result:
    #         output.append()
    print(result)


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def groupAnagrams_3(strs):
    res = defaultdict(list)
    for word in strs:
        key = str(sorted(word))
        res[key].append(word)
    return list(res.values())


print(groupAnagrams_3(strs))


num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
