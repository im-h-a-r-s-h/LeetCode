# LeetCode Problem: Maximum Nesting Depth of the Parentheses
# Problem Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/?envType=problem-list-v2&envId=stack

class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        maxi=0
        for i in s:
            if i=="(":
                stack.append("(")
            if i==")":
                stack.pop()
            maxi=max(maxi,len(stack))
        return maxi
            
