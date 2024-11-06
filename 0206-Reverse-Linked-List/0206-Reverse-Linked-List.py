# LeetCode Problem: 206-Reverse-Linked-List

# Problem Link: https://leetcode.com/problems/reverse-linked-list/
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
