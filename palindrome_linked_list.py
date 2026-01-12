
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr_node = ListNode()
        curr_node = head
        s = []

        while curr_node:
            s.append(curr_node.val)
            curr_node = curr_node.next
        
        while head:
            c = s.pop()
            if head.val != c:
                return False
            head = head.next

        return True


        
        

        
