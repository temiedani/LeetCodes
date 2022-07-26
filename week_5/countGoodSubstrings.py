# LeetCode 1876. Substrings of Size Three with Distinct Characters
'''
A string is good if there are no repeated characters.
Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
Note that if there are multiple occurrences of the same substring, 
every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.
'''


class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        windowSize = 3
        output = 0
        start = 0
        end = windowSize-1
        while end < len(s):
            print(s[start:end+1])
            if len(s[start:end+1]) == len(set(s[start:end+1])):
                output += 1
            start += 1
            end += 1
        return output


'''
Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".

Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
'''
