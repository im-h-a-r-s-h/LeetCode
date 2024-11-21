# LeetCode Problem: 3184-Count-Pairs-That-Form-a-Complete-Day-I
# Problem Link: https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/description/?envType=problem-list-v2&envId=hash-table

# Solution 1: Using Bruteforce 
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt=0
        for i in range(0,len(hours)-1):
            for j in range(i+1,len(hours)):
                if (hours[i]+hours[j])%24==0:
                    cnt+=1
        return cnt
