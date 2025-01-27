# LeetCode Problem: 2869-Minimum-Operations-to-Collect-Elements
# Problem Link: https://leetcode.com/problems/minimum-operations-to-collect-elements/description/?envType=problem-list-v2&envId=hash-table

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        d={}
        cnt=0
        maxi=0
        for i in range(len(nums)-1,-1,-1):
            cnt+=1
            if (nums[i] in d) or nums[i]>k:
                continue
            else:
                d[nums[i]]=cnt
                if d[nums[i]]:
                    maxi=max(maxi,cnt)
        return maxi
        
            

