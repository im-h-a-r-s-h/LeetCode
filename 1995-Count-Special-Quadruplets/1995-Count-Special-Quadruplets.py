# LeetCode Problem: 1995-Count-Special-Quadruplets
# Problem Link: https://leetcode.com/problems/count-special-quadruplets/description/
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        numbers = {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                s = nums[j] + nums[i]
                if s not in numbers:
                    numbers[s] = []
                numbers[s].append(j)

        for i in range(2, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                target = nums[j] - nums[i]
                if target in numbers:
                    for idx in numbers[target]:
                        if idx < i:
                            count += 1
        return count

            
