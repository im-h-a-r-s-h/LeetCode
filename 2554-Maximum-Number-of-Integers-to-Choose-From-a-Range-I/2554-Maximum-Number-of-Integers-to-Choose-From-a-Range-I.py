# LeetCode Problem: 2554-Maximum-Number-of-Integers-to-Choose-From-a-Range-I
# Problem Link: https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description/
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        d=set(banned)
        sumi=0
        cnt=0
        for i in range(1,n+1):
            if i in d:
                continue
            if maxSum>=sumi+i:
                sumi+=i
                cnt+=1
        return cnt
        
