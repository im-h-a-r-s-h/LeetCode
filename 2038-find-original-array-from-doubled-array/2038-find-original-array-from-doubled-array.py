# LeetCode Problem: 2038. Find Original Array From Doubled Array
# Problem Link: https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        changed.sort()
        d = {}
        for i in changed:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        ans = []
        for i in changed:
            if d[i] == 0:
                continue
            if (i * 2 not in d) or d[i * 2] == 0:
                return []
            d[i] -= 1
            d[i * 2] -= 1
            ans.append(i)
        if len(ans) == n // 2:
            return ans
        else:
            return []
