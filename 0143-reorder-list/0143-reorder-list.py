class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow
        y, aux = second.next, second.next
        
        second.next = None
        while y and aux:
            aux = y.next
            y.next = second
            second = y
            y = aux
      
        x, tmp1, tmp2 = head, head.next, second.next
        while tmp2 and second:
            x.next = second
            second.next = tmp1
            x = tmp1
            second = tmp2
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        