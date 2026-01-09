class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # Remove leading nodes with value == val
        while head and head.val == val:
            head = head.next

        t = head
        while t and t.next:
            if t.next.val == val:
                t.next = t.next.next
            else:
                t = t.next

        return head
