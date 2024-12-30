Problem Name: 2190-Most-Frequent-Number-Following-Key-In-an-Array
Problem Link: https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/description/?envType=problem-list-v2&envId=hash-table

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d = {}
        for i in range(len(nums)-1):
            if nums[i] == key:
                if nums[i + 1] in d:
                    d[nums[i + 1]] += 1
                else:
                    d[nums[i + 1]] = 1

        a = None
        for k, v in d.items():
            if not a or a[1] < v:
                a = (k, v)
        
        return a[0]
