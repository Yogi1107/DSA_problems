# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Initialize two pointers
        slow = head     # moves one step at a time
        fast = head     # moves two steps at a time

        # Traverse the list
        while fast and fast.next:

            # Move slow pointer by 1
            slow = slow.next

            # Move fast pointer by 2
            fast = fast.next.next

            # If both pointers meet, a cycle exists
            if slow == fast:
                return True

        # If fast reaches the end, no cycle exists
        return False
