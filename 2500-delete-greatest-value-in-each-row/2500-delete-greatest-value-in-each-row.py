# LeetCode Problem: 2500. Delete Greatest Value in Each Row
# Problem Link: https://leetcode.com/problems/delete-greatest-value-in-each-row/

class Solution:
    import heapq
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans=[-1]*len(grid[0])
        for i in range(len(grid)):
            h=[]
            for j in grid[i]:
                heapq.heappush(h,-j)
            for j in range(len(grid[0])):
                ans[j]=max(ans[j],-heapq.heappop(h))
        return sum(ans)
