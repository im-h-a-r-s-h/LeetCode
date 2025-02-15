# LeetCode Problem: 2866. Beautiful Towers I
# Problem Link: https://leetcode.com/problems/beautiful-towers-i/

class Solution:
    import heapq
    def minOperations(self, nums: List[int], k: int) -> int:
        h=[]
        for i in nums:
            heapq.heappush(h,i)
        cnt=0
        while(len(h)>1):
            x=heapq.heappop(h)
            y=heapq.heappop(h)
            if x>=k:
                break
            heapq.heappush(h,(x*2)+y)
            cnt+=1
        return cnt
