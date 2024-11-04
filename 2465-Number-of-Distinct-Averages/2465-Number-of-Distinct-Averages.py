# LeetCode Problem: 2465-Number-of-Distinct-Averages
# Problem Link: https://leetcode.com/problems/number-of-distinct-averages/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        d={}
        cnt=0
        while(len(nums)>0):
            a=max(nums)
            nums.remove(a)
            b=min(nums)
            nums.remove(b)
            avg=(a+b)/2
            if avg in d:
                d[avg]+=1
            else:
                d[avg]=1
                cnt+=1
        return cnt
