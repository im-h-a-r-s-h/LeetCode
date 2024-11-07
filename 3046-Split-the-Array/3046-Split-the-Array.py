# LeetCode Problem: 3046-Split-the-Array
# Problem Link: https://leetcode.com/problems/split-the-array/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if len(nums)%2!=0:
            return False
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j>2:
                return False
        return True
