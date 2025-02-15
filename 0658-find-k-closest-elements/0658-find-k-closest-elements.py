# LeetCode Problem: 658. Find K Closest Elements
# Problem Link: https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    import heapq
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h=[]
        for i in arr:
            t=i-x
            if i-x<0:
                t=-t
            heapq.heappush(h,(t,i))
        ans=[]
        while(k):
            i,j=heapq.heappop(h)
            ans.append(j)
            k-=1
        return sorted(ans)
