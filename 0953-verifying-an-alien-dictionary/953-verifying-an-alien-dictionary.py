# LeetCode Problem: 953. Verifying an Alien Dictionary
# Problem Link: https://leetcode.com/problems/verifying-an-alien-dictionary/

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        cnt = 0
        d = {}
        for i in order:
            d[i] = cnt
            cnt += 1
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    if d[words[i][j]] > d[words[i + 1][j]]:
                        return False
                    break
            else:
                if len(words[i]) > len(words[i + 1]):
                    return False
        return True
