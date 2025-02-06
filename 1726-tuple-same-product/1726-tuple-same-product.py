# LeetCode Problem: 1726. Tuple with Same Product
# Problem Link: https://leetcode.com/problems/tuple-with-same-product/

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] * nums[j] in d:
                    ans += 8 * d[nums[i] * nums[j]]
                    d[nums[i] * nums[j]] += 1
                else:
                    d[nums[i] * nums[j]] = 1
        return ans
