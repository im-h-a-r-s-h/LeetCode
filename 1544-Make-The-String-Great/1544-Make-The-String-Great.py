# LeetCode Problem: Make The String Great
# Problem Link: https://leetcode.com/problems/make-the-string-great/description/?envType=problem-list-v2&envId=stack&difficulty=EASY

# Approach 1: Using stack
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if i.islower():
                if len(stack) and stack[-1].isupper() and stack[-1].lower() == i:
                    stack.pop()
                else:
                    stack.append(i)
            elif i.isupper():
                if len(stack) and stack[-1].islower() and stack[-1].upper() == i:
                    stack.pop()
                else:
                    stack.append(i)
        ans = ""
        for i in stack:
            ans += i
        
        return ans
