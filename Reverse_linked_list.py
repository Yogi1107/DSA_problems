class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_ = curr.next      # store next node
            curr.next = prev       # reverse link
            prev = curr            # move prev forward
            curr = next_           # move curr forward

        return prev
