# LeetCode Problem: 2956-Find-Common-Elements-Between-Two-Arrays
# Problem Link: https://leetcode.com/problems/find-common-elements-between-two-arrays/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[0,0]
        d={}
        for i in nums1:
            d[i]=1
        for i in nums2:
            if i in d:
                ans[1]+=1
        d={}
        for i in nums2:
            d[i]=1
        for i in nums1:
            if i in d:
                ans[0]+=1     
        return ans
