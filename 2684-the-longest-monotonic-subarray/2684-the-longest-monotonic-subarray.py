# LeetCode Problem: 2684. The Longest Monotonic Subarray
# Problem Link: https://leetcode.com/problems/the-longest-monotonic-subarray/

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 1
        mlen = 1
        dec_len = 1
        inc_len = 1
        while r < n:
            if nums[r - 1] > nums[r]:
                dec_len += 1
                inc_len = 1
            elif nums[r - 1] < nums[r]:
                inc_len += 1
                dec_len = 1
            else:
                l = r
                dec_len = 1
                inc_len = 1
            r += 1
            mlen = max(dec_len, inc_len, mlen)
        return mlen
