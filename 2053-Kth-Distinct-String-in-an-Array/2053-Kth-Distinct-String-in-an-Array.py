# LeetCode Problem: 2053-Kth-Distinct-String-in-an-Array
# Problem Link: https://leetcode.com/problems/kth-distinct-string-in-an-array/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        cnt=0
        for i,j in d.items() :
            if j==1:
                cnt+=1
                if cnt==k:
                    return i
        return ""
            
