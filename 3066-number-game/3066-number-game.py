# LeetCode Problem: 3066. Number Game
# Problem Link: https://leetcode.com/problems/number-game/

import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        h=[]
        for i in nums:
            heapq.heappush(h,i)
        arr=[]
        while(len(h)):
            i=heapq.heappop(h)
            j=heapq.heappop(h)
            arr.append(j)
            arr.append(i)
        return arr
