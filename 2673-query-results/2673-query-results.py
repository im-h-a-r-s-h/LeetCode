# LeetCode Problem: 2673. Query K-th Smallest Trimmed Number
# Problem Link: https://leetcode.com/problems/query-k-th-smallest-trimmed-number/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        x = {}
        y = {}
        ans = []
        for i, j in queries:
            if i in x:
                old_color = x[i]
                y[old_color] -= 1
                if y[old_color] == 0:
                    del y[old_color]    
            x[i] = j
            if j in y:
                y[j] += 1
            else:
                y[j] = 1
            ans.append(len(y))
        return ans
