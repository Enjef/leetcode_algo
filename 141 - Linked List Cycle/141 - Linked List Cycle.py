# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while fast:
            if slow == fast:
                return True
            if fast.next is None:
                break
            slow = slow.next
            fast = fast.next.next
        return False