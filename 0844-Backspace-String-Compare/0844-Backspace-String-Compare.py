# LeetCode Problem: Backspace String Compare
# Problem Link: https://leetcode.com/problems/backspace-string-compare/?envType=problem-list-v2&envId=stack

# Approach 1: Using stack
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for i in s:
            if i=='#':
                if len(stack1)!=0:
                    stack1.pop()
            else:
                stack1.append(i)
        for i in t:
            if i=='#':
                if len(stack2)!=0:
                    stack2.pop()
            else:
                stack2.append(i)
        if stack1==stack2:
            return True
        else:
            return False
        
