# LeetCode Problem: 2367-Number-of-Arithmetic-Triplets
# Problem Link: https://leetcode.com/problems/number-of-arithmetic-triplets/description/
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set = set(nums)
        count = 0

        for num in nums:
            # Check if the other two elements of the triplet exist
            if (num - diff in nums_set) and (num + diff in nums_set):
                count += 1
        
        return count
        
