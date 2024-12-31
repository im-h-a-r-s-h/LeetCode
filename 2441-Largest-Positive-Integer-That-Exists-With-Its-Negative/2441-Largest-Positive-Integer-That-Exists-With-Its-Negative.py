# LeetCode Problem: 2441-Largest-Positive-Integer-That-Exists-With-Its-Negative
# Problem Link: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d=set(nums)
        maxi=-1
        for i in nums:
            if -1*i in d:
                maxi=max(maxi,abs(i))
        return maxi

        
