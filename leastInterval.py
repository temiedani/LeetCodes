from collections import Counter


def leastInterval(tasks, n):
    output = []
    res = Counter(tasks)
    # res = dict(sorted(dict(res), key=lambda kv: kv[1]))

    for t in res:
        i = 0
        while i < n:
            if t not in output[-n:]:
                output.append(t)
                i += 1
                continue
            else:

                i += 1
    return res


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    # print(leastInterval(tasks, n))
    print(tasks[-n:])
