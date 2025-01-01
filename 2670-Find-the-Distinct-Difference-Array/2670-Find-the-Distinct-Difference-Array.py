# LeetCode Problem: 2670-Find-the-Distinct-Difference-Array
# Problem Link: https://leetcode.com/problems/find-the-distinct-difference-array/description/

Approach 1. using hashmap

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        diff=[0]*n
        d2={}
        dl1=len(d)
        dl2=len(d2)
        for i in range(n):
            d[nums[i]]-=1
            if d[nums[i]]==0:
                del d[nums[i]]
                dl1-=1

            if nums[i] not in d2:
                d2[nums[i]]=1
                dl2+=1
                
            diff[i]=dl2-dl1
        return diff

Approach 2. using set
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        diff=[0]*n
        for i in range(n):
            l=len(set(nums[0:i+1]))
            r=len(set(nums[i+1:]))
            # print(l,r)
            diff[i]=l-r
        return diff
