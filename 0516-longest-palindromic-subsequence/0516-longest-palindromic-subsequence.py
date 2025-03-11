# LeetCode Problem: 516. Longest Palindromic Subsequence
# Problem Link: https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        text2=s[::-1]
        # t=[[0]*(1000) for i in range(1000)]
        t = [[0] * (n + 1) for _ in range(n + 1)] 
        for i in range(n):
            for j in range(n):
                if s[i]==text2[j]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        return t[n-1][n-1]
