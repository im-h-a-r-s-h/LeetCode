# LeetCode Problem: 3356. Minimum Queries to Make Array Zero
# Problem Link: https://leetcode.com/problems/minimum-queries-to-make-array-zero/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def is_valid(nums,que,k):
            n = len(nums)
            dist = [0] * (n + 1)
            for i in range(k + 1):
                l, r, val = que[i]
                dist[l] += val
                if r + 1 < len(dist):
                    dist[r + 1] -= val
            for i in range(1, n):
                dist[i] += dist[i - 1]
            for i in range(n):
                if nums[i] - dist[i] > 0:
                    return False
            return True

        if all(x == 0 for x in nums):
            return 0
        l, h= 0, len(queries)- 1
        ans=-1
        while l <= h:
            mid = (l + h) // 2
            if is_valid(nums, queries, mid):
                ans = mid + 1
                h = mid - 1
            else:
                l = mid + 1
        return ans
        
