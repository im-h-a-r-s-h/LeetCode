# LeetCode Problem: Remove All Adjacent Duplicates In String
# Problem Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for i in s:
            if len(stack) and i==stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        ans=""
        for i in stack:
            ans+=i
        return ans
