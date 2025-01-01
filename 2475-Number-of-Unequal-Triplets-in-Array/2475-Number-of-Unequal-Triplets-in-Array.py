# LeetCode Problem: 2475-Number-of-Unequal-Triplets-in-Array
# Problem Link: https://leetcode.com/problems/number-of-unequal-triplets-in-array/description/?envType=problem-list-v2&envId=hash-table

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        total, left, right = 0, 0, len(nums)
        for key in d:
            count = d[key]
            right -= count
            total += left * count * right
            left += count
        
        return total

APPROACH 2:

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        count += 1
        return count
