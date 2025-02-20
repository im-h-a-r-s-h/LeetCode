# LeetCode Problem: 1980. Find Unique Binary String
# Problem Link: https://leetcode.com/problems/find-unique-binary-string/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        d = set(nums)
        
        def back(s):
            if len(s) == n:
                candidate = ''.join(s)
                if candidate not in d:
                    return candidate
                return None  # Ensure backtracking continues

            for i in ['0', '1']:
                s.append(i)
                res = back(s)
                if res:  # If a valid string is found, return immediately
                    return res
                s.pop()

        return back([])
