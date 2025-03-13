# LeetCode Problem: 494. Target Sum
# Problem Link: https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def countSubsetSum(nums, tar):
            n = len(nums)
            t = [[0] * (tar + 1) for _ in range(n + 1)]
            for i in range(n + 1):
                t[i][0] = 1

            for i in range(1, n + 1):
                for j in range(tar + 1):
                    if nums[i - 1] <= j:
                        t[i][j] = t[i - 1][j - nums[i - 1]] + t[i - 1][j]
                    else:
                        t[i][j] = t[i - 1][j]          
            return t[n][tar]

        total_sum = sum(nums)
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0
        tar = (total_sum + target) // 2
        return countSubsetSum(nums, tar)

