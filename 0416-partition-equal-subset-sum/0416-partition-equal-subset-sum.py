# LeetCode Problem: 416. Partition Equal Subset Sum
# Problem Link: https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subset_sum(nums,tar):
            n=len(nums)
            t=[[False] *(tar+1) for i in range(n+1)]

            for i in range(n+1):
                for j in range(tar+1):
                    if i==0:
                        t[i][j]=False
                    if j==0:
                        t[i][j]=True

            for i in range(1,n+1):
                for j in range(1,tar+1):
                    if nums[i-1]<=j:
                        t[i][j]=t[i-1][j-nums[i-1]] or t[i-1][j]
                    else:
                        t[i][j]=t[i-1][j]          
            return t[n][tar]
        sumi=sum(nums)
        if sumi%2!=0:
            return False
        else:
            return subset_sum(nums,sumi//2)
