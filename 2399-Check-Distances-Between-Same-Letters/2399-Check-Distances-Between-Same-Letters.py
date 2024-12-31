# LeetCode Problem: 2399-Check-Distances-Between-Same-Letters
# Problem Link: https://leetcode.com/problems/check-distances-between-same-letters/description/
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d={}
        for i in range(len(s)):
            if s[i] in d:
                di=i-d[s[i]]-1
                d[s[i]]=di
            else:
                d[s[i]]=i
        for i,j in d.items():
            if distance[ord(i)-97]!=j:
                return False
        return True
        
