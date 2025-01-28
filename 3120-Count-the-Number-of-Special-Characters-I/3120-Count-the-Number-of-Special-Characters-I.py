# LeetCode Problem: 3120-Count-the-Number-of-Special-Characters-I
# Problem Link: https://leetcode.com/problems/count-the-number-of-special-characters-i/
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d={}
        for i in word:
            if i.isupper():
                t=chr(ord(i)+32)
            else:
                t=i
            if t in d:
                d[t].add(i)
            else:
                d[t]=set(i)
        cnt=0
        for i,j in d.items():
            if len(j)==2:
                cnt+=1
        return cnt
