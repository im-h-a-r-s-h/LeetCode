# LeetCode Problem: 2729-Check-if-the-Number-is-Fascinating
# Problem Link: https://leetcode.com/problems/check-if-the-number-is-fascinating/description/?envType=problem-list-v2&envId=hash-table&status=TO_DO&difficulty=EASY
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next  
            curr.next = prev   
            prev = curr           
            curr = next_temp       
        return prev
