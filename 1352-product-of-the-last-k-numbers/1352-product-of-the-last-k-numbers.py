# LeetCode Problem: 1352. Product of the Last K Numbers
# Problem Link: https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers:
    def __init__(self):
        self.stream=[]

    def add(self, num: int) -> None:
        if num==0:
            self.stream=[]
        elif self.stream==[]:
            self.stream.append(num)
        else:
            self.stream.append(num*self.stream[-1])
        
    def getProduct(self, k: int) -> int:
        n=len(self.stream)
        if n<k:
            return 0
        elif n==k:
            return self.stream[-1]
        else:
            return self.stream[-1]//self.stream[-1-k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
