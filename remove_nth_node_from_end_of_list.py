# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        new_prev = None
        counter = 1

        while prev:
            if counter == n:
                prev = prev.next
                if prev == None:
                    break

            nxt = prev.next
            prev.next = new_prev
            new_prev = prev
            prev = nxt

            counter += 1
        return new_prev
        
