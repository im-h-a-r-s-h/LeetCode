# LeetCode Problem: 1848-Minimum-Distance-to-the-Target-Element
# Problem Link: https://leetcode.com/problems/minimum-distance-to-the-target-element/description/

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mini=10**9
        for i in range(len(nums)):
            if nums[i]==target:
                mini=min(abs(i-start),mini)
        return mini
            
