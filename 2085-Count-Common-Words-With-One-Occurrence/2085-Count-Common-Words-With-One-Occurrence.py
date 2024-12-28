# LeetCode Problem: 2085-Count-Common-Words-With-One-Occurrence
# Problem Link: https://leetcode.com/problems/count-common-words-with-one-occurrence/description/
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d={}
        cnt=0
        for i in words1:
            if i in d:
                d[i]=-1
            else:
                d[i]=0

        for i in words2:
            if i in d and d[i]==0: 
                d[i]=1
                cnt+=1
            elif i in d and d[i]==1: 
                d[i]=-1
                cnt-=1
        return cnt
