# LeetCode Problem: 2037-Minimum-Number-of-Moves-to-Seat-Everyone
# Problem Link: https://leetcode.com/problems/baseball-game/description/

# Approach 1: Using greedy approach
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        cnt=0
        for i in range(len(students)):
            cnt+=abs(seats[i]-students[i])
        return cnt
