# LeetCode Problem: 2570-Merge-Two-2D-Arrays-by-Summing-Values
# Problem Link: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d={}
        for i,j in nums1:
            if i in d:
                d[i]+=j
            else:
                d[i]=j
        for i,j in nums2:
            if i in d:
                d[i]+=j
            else:
                d[i]=j
        ans=[]
        for i,j in d.items():
            ans.append([i,j])
        ans.sort(key=lambda x: x[0])
        return ans
