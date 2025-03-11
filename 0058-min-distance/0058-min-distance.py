# LeetCode Problem: 58. Edit Distance
# Problem Link: https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        t=[[0]*(1000) for i in range(1000)]
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i]==word2[j]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        k= t[len(word1)-1][len(word2)-1]
        return len(word1)+len(word2)-(2*k)
        
