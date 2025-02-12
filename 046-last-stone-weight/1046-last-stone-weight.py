class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=[]
        for i in stones:
            heapq.heappush(h,-i)
        while(len(h)>1):
            i=-heapq.heappop(h)
            j=-heapq.heappop(h)
            if i!=j:
                heapq.heappush(h,-(i-j))
        if len(h)==1:
            return -h[0]
        else:
            return 0
