# LeetCode Problem: Clear Digits
# Problem Link: https://leetcode.com/problems/clear-digits/description/?envType=problem-list-v2&envId=stack

class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in s:
            if i.isdigit():
                if len(stack)!=0:
                    stack.pop()
            else:
                stack.append(i)
        ans=""
        for i in stack:
            ans+=i
        return ans
            
