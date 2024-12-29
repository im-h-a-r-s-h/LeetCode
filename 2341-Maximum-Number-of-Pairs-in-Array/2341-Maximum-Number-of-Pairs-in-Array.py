# LeetCode Problem: 2341-Maximum-Number-of-Pairs-in-Array
# Problem Link: https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/?envType=problem-list-v2&envId=hash-table
# Approach 1: Two traversal
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        cnt=0
        rem=0
        for i,j in d.items():
            cnt+=j//2
            rem+=j%2
        return [cnt,rem]
