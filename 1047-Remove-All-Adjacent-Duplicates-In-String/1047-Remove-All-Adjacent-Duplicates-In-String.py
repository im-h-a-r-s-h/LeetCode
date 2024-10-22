# LeetCode Problem: Remove All Adjacent Duplicates In String
# Problem Link: https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i * 2 in d:
                d[i * 2] += 1
            else:
                d[i * 2] = 1
        for i in arr:
            if i == 0:
                if d[0] > 1:
                    return True
            else:
                if i in d:
                    return True
        return False
