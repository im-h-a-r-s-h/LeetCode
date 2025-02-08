
# Code
```python
# LeetCode Problem: 2349. Design a Number Container System
# Problem Link: https://leetcode.com/problems/design-a-number-container-system/

import heapq

class NumberContainers:
    def __init__(self):
        self.d = {}  # Maps numbers to min-heaps of indices
        self.ind = {}  # Maps indices to numbers
        
    def change(self, index: int, number: int) -> None:
        if index in self.ind and self.ind[index] == number:
            return 
        
        self.ind[index] = number
        if number in self.d:
            heapq.heappush(self.d[number], index)
        else:
            self.d[number] = [index]
        
    def find(self, number: int) -> int:
        if number not in self.d:
            return -1
        while self.d[number]:
            if number == self.ind[self.d[number][0]]:
                return self.d[number][0]
            else:
                heapq.heappop(self.d[number])
        return -1
