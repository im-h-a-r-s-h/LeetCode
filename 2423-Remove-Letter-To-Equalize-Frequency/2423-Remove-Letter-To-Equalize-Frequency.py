# LeetCode Problem: 2423-Remove-Letter-To-Equalize-Frequency
# Problem Link: https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        d = {}
        for i in word:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for char in list(d.keys()):
            d[char] -= 1
            if d[char] == 0:
                del d[char]
            if len(set(d.values())) == 1:
                return True
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        return False
