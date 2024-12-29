# LeetCode Problem: 160-Intersection-of-Two-Linked-Lists
# Problem Link: https://leetcode.com/problems/intersection-of-two-linked-lists/?source=submission-noac
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ca = 0
        temp = headA
        while temp:
            ca += 1
            temp = temp.next

        cb = 0
        temp = headB
        while temp:
            cb += 1
            temp = temp.next

        t1 = headA
        t2 = headB

        if ca > cb:
            for _ in range(ca - cb):
                t1 = t1.next
        else:
            for _ in range(cb - ca):
                t2 = t2.next

        while t1 and t2:
            if t1 == t2:
                return t1
            t1 = t1.next
            t2 = t2.next

        return None
