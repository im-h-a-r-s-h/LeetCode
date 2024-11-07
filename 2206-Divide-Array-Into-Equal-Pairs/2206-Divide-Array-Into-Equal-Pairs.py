# LeetCode Problem: 2206-Divide-Array-Into-Equal-Pairs
# Problem Link: https://leetcode.com/problems/divide-array-into-equal-pairs/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j%2!=0:
                return False
        return True
