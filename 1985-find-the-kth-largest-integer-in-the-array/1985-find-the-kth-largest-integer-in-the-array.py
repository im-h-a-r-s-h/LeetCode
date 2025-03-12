# LeetCode Problem: 1985. Find the Kth Largest Integer in the Array
# Problem Link: https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    import heapq
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        h=[]
        for i in nums:
            heapq.heappush(h,int(i))
            if len(h)>k:
                heapq.heappop(h)
        return str(h[0])
        
