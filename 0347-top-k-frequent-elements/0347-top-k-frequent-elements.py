# LeetCode Problem: 347. Top K Frequent Elements
# Problem Link: https://leetcode.com/problems/top-k-frequent-elements/

APPROACH 1: using bucket sort

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        bucket=[]
        for i in range(len(nums)+1):
            bucket.append([])
        for i,j in d.items():
            bucket[j].append(i)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res


APPROACH 2: using heap queue:

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in  nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        heap=[]
        for i,j in d.items():
            heapq.heappush(heap,(j,i))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for value,key in heap:
            res.append(key)
        return res


