# LeetCode Problem: 3158. Find the XOR of Numbers Which Appear Twice
# Problem Link: https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/
class Solution:
    def xorOfNumbers(self, nums: List[int]) -> int:
        n = set()
        x = 0
        for i in nums:
            if i in n:
                x ^= i
            else:
                n.add(i)
        return x

