# LeetCode Problem: Top K Frequent Words
# Problem Link: https://leetcode.com/problems/top-k-frequent-words/description/?envType=problem-list-v2&envId=hash-table

from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for i in words:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        sd = dict(sorted(d.items(), key=lambda item: (-item[1], item[0])))
        
        res = []
        for i in sd:
            res.append(i)
            k -= 1
            if k == 0:
                break
        
        return res
