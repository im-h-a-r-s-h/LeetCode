# LeetCode Problem: Remove Outermost Parentheses
# Problem Link: https://leetcode.com/problems/remove-outermost-parentheses/description/?envType=problem-list-v2&envId=stack&difficulty=EASY

# Approach 1: Using stack
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ""
        count = 0
        for i in s:
            if i == "(":
                if count > 0:  
                    ans += i
                count += 1
            if i == ")":
                count -= 1
                if count > 0: 
                    ans += i
        return ans
        
