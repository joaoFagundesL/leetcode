# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p = q = dummy
        for _ in range(n): p = p.next
        while p.next: p, q = p.next, q.next
        r = q.next
        q.next = r.next
        del r
        return dummy.next