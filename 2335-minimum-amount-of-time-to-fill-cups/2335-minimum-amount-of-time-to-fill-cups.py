# LeetCode Problem: 2335. Minimum Amount of Time to Fill Cups
# Problem Link: https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

class Solution:
    import heapq
    def fillCups(self, amount: List[int]) -> int:
        h=[]
        time=0
        for i in amount:
            if i > 0: 
                heapq.heappush(h, -i)
        while(len(h)>1):
            maxi1=-heapq.heappop(h)
            maxi2=-heapq.heappop(h)
            time+=1
            if maxi1 - 1 > 0:
                heapq.heappush(h, -(maxi1 - 1))
            if maxi2 - 1 > 0:
                heapq.heappush(h, -(maxi2 - 1))
        if h:  
          time += -h[0]
        return time
