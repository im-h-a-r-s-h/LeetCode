# LeetCode Problem: 1002-Find-Common-Characters
# Problem Link: https://leetcode.com/problems/find-common-characters/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY

# Solution 1: Using hashmap for linear complexity 
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d1=[0]*26
        for i in words[0]:
            d1[ord(i)-97]+=1

        for i in range(1,len(words)):
            d2=[0]*26
            for j in words[i]:
                d2[ord(j)-97]+=1

            for j in range(26):
                d1[j]=min(d1[j],d2[j])
        ans=[]
        for i in range(26):
            while d1[i]!=0:
                ans.append(chr(i+97))
                d1[i]-=1
        return ans


        
        
        
