# LeetCode Problem: 561-Array-Partition
# Problem Link: https://leetcode.com/problems/array-partition/description/
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sumi=0
        for i in range(0,len(nums),2):
            sumi=sumi+nums[i]
        return sumi
            
