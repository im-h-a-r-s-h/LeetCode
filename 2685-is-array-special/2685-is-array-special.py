# LeetCode Problem: 2685. Is Array Special
# Problem Link: https://leetcode.com/problems/is-array-special/

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        temp = False
        prev = True
        if nums[0] % 2 == 0:
            temp = True
            prev = False
        for i in nums:
            if i % 2 == 0:
                temp = True
            else:
                temp = False
            if prev == temp:
                return False
            prev = temp
        return True
