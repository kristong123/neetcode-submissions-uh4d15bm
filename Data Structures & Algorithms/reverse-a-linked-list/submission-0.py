# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        curr = head.next
        first = head
        first.next = None

        while curr:
            node = curr
            curr = curr.next
            node.next = first
            first = node

        return first