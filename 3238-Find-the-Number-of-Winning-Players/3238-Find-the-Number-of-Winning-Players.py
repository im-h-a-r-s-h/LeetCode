# LeetCode Problem: 3238-Find-the-Number-of-Winning-Players
# Problem Link: https://leetcode.com/problems/find-the-number-of-winning-players/description/


# Complexity
- Time complexity:O(N)
- Space complexity:O(N)

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        d={}
        for s in pick:
            i=""
            for j in s:
                i+=str(j)
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=set()
        for i,j in d.items():
            if j>int(i[0]):
                a.add(i[0])
        return len(a)
