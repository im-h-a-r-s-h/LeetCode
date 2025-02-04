# LeetCode Problem: 1800. Maximum Ascending Subarray Sum
# Problem Link: https://leetcode.com/problems/maximum-ascending-subarray-sum/

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 1
        msum = nums[l]
        sumi = nums[l]
        
        while r < n:
            if nums[r - 1] < nums[r]:
                sumi += nums[r]
                msum = max(sumi, msum)
            else:
                l = r
                sumi = nums[l]
            r += 1
        return msum
