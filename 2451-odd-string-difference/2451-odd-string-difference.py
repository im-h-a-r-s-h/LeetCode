# LeetCode Problem: 2451. Odd String Difference
# Problem Link: https://leetcode.com/problems/odd-string-difference/
class Solution:
    def oddString(self, words: List[str]) -> str:
        d = {}
        for i in words:
            temp = []
            for j in range(1, len(i)):
                temp.append(ord(i[j]) - ord(i[j - 1]))
            temp = str(temp)
            if temp in d:
                d[temp][1] = True
            else:
                d[temp] = [i, False]
        for i, j in d.items():
            if not j[1]:
                return j[0]
