# LeetCode Problem: 2357-Make-Array-Zero-by-Subtracting-Equal-Amounts
# Problem Link: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/?envType=problem-list-v2&envId=hash-table

APPROACH 1:
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums)-{0})

APPROACH 2:
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i==0 or (i in d):
                continue
            else:
                d[i]=1
        return len(d)
