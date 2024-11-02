Problem Name: 1370-Increasing-Decreasing-String
Problem Link: https://leetcode.com/problems/increasing-decreasing-string/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY

class Solution:
    def sortString(self, s: str) -> str:
        res=""
        n=len(s)
        d=[0]*26
        for i in s:
            d[ord(i)-97]+=1
        while(True):
            if len(res)==len(s):
                return res
            for i in range(26):
                if d[i]!=0:
                    temp=chr(i+97)
                    d[i]-=1
                    res+=temp
            for i in range(25,-1,-1):
                if d[i]!=0:
                    temp=chr(i+97)
                    d[i]-=1
                    res+=temp
        return res
            

# Complexity
- Time complexity:O(n)
- Space complexity:O(26)
