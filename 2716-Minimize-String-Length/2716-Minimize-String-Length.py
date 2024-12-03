# LeetCode Problem: 2716-Minimize-String-Length
# Problem Link: https://leetcode.com/problems/minimize-string-length/description/?envType=problem-list-v2&envId=hash-table&status=TO_DO&difficulty=EASY
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        d={}
        cnt=0
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                cnt+=1
        return cnt
