# LeetCode Problem: 2109-Adding-Spaces-to-a-String
# Problem Link: https://leetcode.com/problems/adding-spaces-to-a-string/description/?envType=daily-question&envId=2024-12-03
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        temp=""
        spaces=set(spaces)
        for i in range(len(s)):
            if i in spaces:
                temp+=" "
            temp+=s[i]
        s=temp
        return s
