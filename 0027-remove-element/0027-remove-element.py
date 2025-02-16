class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        z=0
        for i in nums:
            if i!=val:
                nums[z]=i
                k+=1
                z+=1
        return k
            
