# LeetCode Problem: 0017-Letter-Combinations-of-a-Phone-Number
# Problem Link: https://leetcode.com/problems/reverse-linked-list/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        def backtrack(combination, digits):
            if not digits:
                res.append(combination)
                return
            for letter in phone[digits[0]]:
                backtrack(combination + letter, digits[1:])
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        backtrack("", digits)
        return res
