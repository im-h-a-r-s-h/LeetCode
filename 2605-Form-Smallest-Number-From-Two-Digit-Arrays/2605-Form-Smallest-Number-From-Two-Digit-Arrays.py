# LeetCode Problem: 2605-Form-Smallest-Number-From-Two-Digit-Arrays
# Problem Link: https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/description/

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        d=set(nums1)
        mini=sys.maxsize
        m1=min(nums1)
        m2=sys.maxsize
        for i in nums2:
            if i in d:
                mini=min(mini,i)
            else:
                m2=min(m2,i)
        s=""
        s+=str(min(m1,m2))
        s+=str(max(m1,m2))
        return min(int(s),mini)        
