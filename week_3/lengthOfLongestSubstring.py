# 3. Longest Substring Without Repeating Characters
'''
Given a string s, 
find the length of the longest substring without repeating characters.
'''


def lengthOfLongestSubstring(s: str) -> int:
    """
    :type s: str
    :rtype: int
    """
    sub = {}
    length = longest = 0
    for idx, ch in enumerate(s):
        if ch in sub.values():
            sub.pop(ch)
        sub[ch] = idx
        length += 1
        longest = max(length, longest)
    return longest


if __name__ == '__main__':
    x = "abcabcbb"
    y = "dvdf"
    z = "pwwkew"
    print(lengthOfLongestSubstring(y))
    sub = {1: 2, 3: 4, 5: 6, 7: 8, 9: 10}
    ss = set()
