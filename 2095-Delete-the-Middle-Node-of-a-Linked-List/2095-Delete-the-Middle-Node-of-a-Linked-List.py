# LeetCode Problem: 2095-Delete-the-Middle-Node-of-a-Linked-List

# Problem Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=problem-list-v2&envId=linked-list
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = slow.next
        return head
