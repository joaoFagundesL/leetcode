class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = self.getMiddle(head)
        second = slow
        second = self.reverseList(second)
      
        x, tmp1, tmp2 = head, head.next, second.next
        while tmp2 and second:
            x.next = second
            second.next = tmp1
            x = tmp1
            second = tmp2
            tmp1 = tmp1.next
            tmp2 = tmp2.next
    
    def getMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        y, aux = head.next, head.next
        head.next = None
        while y and aux:
            aux = y.next
            y.next = head
            head = y
            y = aux
        return head
