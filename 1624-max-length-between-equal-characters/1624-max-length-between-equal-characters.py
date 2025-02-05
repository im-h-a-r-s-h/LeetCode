# LeetCode Problem: 1624. Max Length Between Equal Characters
# Problem Link: https://leetcode.com/problems/max-length-between-equal-characters/

from typing import List

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]].append(i)
            else:
                d[s[i]] = [i]
        maxi = -1
        for i, j in d.items():
            if len(j) > 1:
                maxi = max(maxi, d[i][-1] - d[i][0] - 1)
        return maxi
