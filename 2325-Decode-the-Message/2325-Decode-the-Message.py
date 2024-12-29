# LeetCode Problem: 2325-Decode-the-Message
# Problem Link: https://leetcode.com/problems/decode-the-message/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d={}
        cnt=97
        for i in key:
            if i==" " or (i in d):
                continue
            else:
                d[i]=chr(cnt)
                cnt+=1
        s=""
        for i in message:
            if i==" ":
                s+=" "
                continue
            s+=d[i]
        return s
