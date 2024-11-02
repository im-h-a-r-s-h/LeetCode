# LeetCode Problem: Height-Checker
# Problem Link: https://leetcode.com/problems/height-checker/description/?envType=problem-list-v2&envId=counting-sort

# Solution 1: Using counting sort for 0(n) complexity 
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=[0]*(max(heights)+1)
        n=len(heights)
        output=[0]*n
        for i in heights:
            count[i]+=1

        for i in range(1,len(count)):
            count[i]+=count[i-1]

        ans=0
        for i in range(n-1,-1,-1):
            output[count[heights[i]]-1]=heights[i]
            count[heights[i]]-=1

        for i in range(n-1,-1,-1):
            if output[i]!=heights[i]:
                ans+=1
        return ans

  # Solution 2: Using noraml sorting
  class Solution:
      def heightChecker(self, heights: List[int]) -> int:
          output=heights
          heights.sort()
          for i in range(n-1,-1,-1):
              if output[i]!=heights[i]:
                  ans+=1
          return ans
