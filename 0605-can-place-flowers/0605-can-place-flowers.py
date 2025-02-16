class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return (flowerbed[0] == 0 and n <= 1) or n == 0
        if (flowerbed[0]==0 and flowerbed[1]==0):
            flowerbed[0]=1 
            n-=1
        for i in range(1,len(flowerbed)-1):
            if n==0:
                return True
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        if (flowerbed[-1]==0 and flowerbed[-2]==0):
            n-=1
        return n<=0
