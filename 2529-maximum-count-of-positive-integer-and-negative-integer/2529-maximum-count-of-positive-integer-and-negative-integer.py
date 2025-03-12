# LeetCode Problem: [2529]. Maximum Count of Positive Integer and Negative Integer
# Problem Link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        h=n-1
        ans=[-1,-1]
        while(l<=h):
            mid=(h+l)//2
            if nums[mid] > 0 and (mid == 0 or nums[mid - 1] <= 0):
                ans[0]=n-mid
                break
            elif nums[mid]>0 and nums[mid-1]>0:
                h=mid
            else:
                l=mid+1
        l=0
        h=n-1
        while(l<=h):
            mid=(h+l)//2
            if nums[mid]<0 and (mid == n-1 or nums[mid + 1]>=0):
                ans[1]=mid+1
                break
            elif nums[mid]<0 and (mid == n-1 or nums[mid + 1]<0):
                l=mid+1
            else:
                h=mid-1
        if ans==[-1,-1]:
            return 0
        return max(ans)
