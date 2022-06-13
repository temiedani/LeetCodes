from collections import Counter
import string


def isAnagram(s: str, t: str) -> bool:
    if (len(s) != len(t)):
        return False
    return Counter(s) == Counter(t)
    # return (sorted(s.lower())==sorted(t.lower()))


def isAnagram_2(s: str, t: str) -> bool:
    if (len(s) != len(t)):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1+countS.get(s[i], 0)
        countT[t[i]] = 1+countT.get(t[i], 0)
    for c in countS:
        if(countS[c] != countT.get(c, 0)):
            return False


def isAnagram_3(s, t):
    if (len(s) != len(t)):
        return False
    ss = list(s.lower())
    tt = list(t.lower())
    return sorted(ss) == sorted(tt)


def isAnagram__4(s, t):
    if (len(s) != len(t)):
        return False
    for c in string.ascii_lowercase:
        if s.count(c) != t.count(c):
            return False
    return True
