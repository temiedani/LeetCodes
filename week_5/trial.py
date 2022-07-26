
from collections import defaultdict


def solution(strings, patterns):
    count_dict = {}
    if len(strings) != len(patterns):
        return False
    # for s in strings:
        # count_dict[s]=count_dict.get(s,1)+1
    for s, p in zip(strings, patterns):
        print(s, p)
        if s not in count_dict:
            if p in count_dict.values():
                return False
            count_dict[s] = p
        else:
            if count_dict[s] != p:
                return False
    print(count_dict)
    return True


strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "b"]

# print(solution(strings, patterns))
nums = [0, 1, 2, 3, 5, 2]
mydict = {}
for i, v in enumerate(nums):
    if v not in mydict:
        mydict[v] = [i]
    else:
        mydict[v].append(i)
# print(mydict.values())
a = "temie"
pieces = [[1, 2], [5], [6, 3], [34, 23]]
print(sum([len(p) for p in pieces]))

df = defaultdict(list)
df[1] = "lol"
print(df.get(1,"does not exist"))
