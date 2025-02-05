# LeetCode Problem: 2679. Find Valid Pair
# Problem Link: https://leetcode.com/problems/find-valid-pair/

from typing import List

class Solution:
    def findValidPair(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in range(1, len(s)):
            if s[i-1] != s[i] and int(s[i-1]) == d[s[i-1]] and int(s[i]) == d[s[i]]:
                return s[i-1] + s[i]
        return ""
