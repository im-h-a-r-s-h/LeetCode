# LeetCode Problem: 2342. Max Sum of a Pair With Equal Sum of Digits
# Problem Link: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumi(n):
            s=str(n)
            sumi=0
            for i in s:
                sumi+=int(i)
            return sumi
        d={}
        for i in nums:
            j=sumi(i)
            if j in d:
                heapq.heappush(d[j],i)
                if len(d[j])>2:
                    heapq.heappop(d[j])
            else:
                d[j]=[i]
        smi=-1
        for i,j in d.items():
            if len(j)>1:
                smi=max(smi,sum(j))
        return smi
