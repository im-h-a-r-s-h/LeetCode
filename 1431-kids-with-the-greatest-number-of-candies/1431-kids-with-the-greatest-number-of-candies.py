# LeetCode Problem: 1431. Kids With the Greatest Number of Candies
# Problem Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        ans=[]
        for i in candies:
            if i+extraCandies>=maxi:
                ans.append(True)
            else:
                ans.append(False)
        return ans
