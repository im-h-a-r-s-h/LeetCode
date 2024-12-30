# LeetCode Problem: 2103-Rings-and-Rods
# Problem Link: https://leetcode.com/problems/rings-and-rods/description/?envType=problem-list-v2&envId=hash-table

class Solution:
    def countPoints(self, rings: str) -> int:
        d={}
        for i in range(1,len(rings),2):
            if rings[i] in d:
                d[rings[i]].add(rings[i-1])
            else:
                d[rings[i]]=set(rings[i-1])
        cnt=0
        for i,j in d.items():
            if len(j)==3:
                cnt+=1
        return cnt

