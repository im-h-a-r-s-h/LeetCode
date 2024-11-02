# LeetCode Problem: 409-Longest-Palindrome
# Problem Link: https://leetcode.com/problems/longest-palindrome/description/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=0
        temp=False
        for i in d.values():
            if i==1 or i%2==1:
                i-=1
                temp=True
            ans+=i
        if temp:
            return ans+1
        else:
            return ans
        
            
