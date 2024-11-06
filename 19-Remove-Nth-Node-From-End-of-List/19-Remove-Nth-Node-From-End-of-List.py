# LeetCode Problem: 19-Remove-Nth-Node-From-End-of-List
# Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s=head
        f=head
        for i in range(n):
            f=f.next
        if f is None:
            return head.next
        while(f!=None and f.next!=None):
            s=s.next
            f=f.next
        s.next=s.next.next
        return head
            
