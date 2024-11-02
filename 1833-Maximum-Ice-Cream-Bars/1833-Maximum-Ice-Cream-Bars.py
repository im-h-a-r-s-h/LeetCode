# LeetCode Problem: 1833-Maximum-Ice-Cream-Bars
# Problem Link: https://leetcode.com/problems/maximum-ice-cream-bars/description/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count=[0]*(max(costs)+1)
        n=len(costs)
        output=[0]*n
        for i in costs:
            count[i]+=1
        for i in range(1,len(count)):
            count[i]+=count[i-1]
        ans=0
        for i in range(n-1,-1,-1):
            output[count[costs[i]]-1]=costs[i]
            count[costs[i]]-=1
        for i in output:
            if i>coins:
                return ans
            else:
                ans+=1
                coins-=i
        return ans
