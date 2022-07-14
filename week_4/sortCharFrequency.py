
def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    count = {}
    for i, v in enumerate(s):
        count[v] = count.get(v, 0) + 1
    print(sorted(count, key=lambda x: x[0]))
    res = [k*v for k, v in count.items()]
    # return "".join(["1", "2", "3"])
    return "".join(res[::-1])


if __name__ == "__main__":
    print(frequencySort("tree"))
