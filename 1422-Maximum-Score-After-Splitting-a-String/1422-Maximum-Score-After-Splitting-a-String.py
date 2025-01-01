# LeetCode Problem: 1422-Maximum-Score-After-Splitting-a-String
# Problem Link: https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/

class Solution:
    def maxScore(self, s: str) -> int:
        zero=0
        ones=0
        if s[0]=="0":
            zero+=1
        for i in range(1,len(s)):
            if s[i]=="1":
                ones+=1
        maxi=zero+ones
        for i in range(1,len(s)-1):
            if s[i]=="1":
                ones-=1
            else:
                zero+=1
            maxi=max(maxi,ones+zero)
        return maxi
