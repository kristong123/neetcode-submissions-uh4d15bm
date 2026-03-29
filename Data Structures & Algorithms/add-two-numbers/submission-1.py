# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        curr = result
        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1 and curr2:
            total = curr1.val + curr2.val + carry
            curr.next = ListNode(total % 10)
            carry = 1 if total > 9 else 0
            curr1 = curr1.next
            curr2 = curr2.next
            curr = curr.next

        rest = curr1 if curr1 else curr2

        while rest:
            total = rest.val + carry
            curr.next = ListNode(total % 10)
            carry = 1 if total > 9 else 0
            rest = rest.next
            curr = curr.next

        if carry == 1:
            curr.next = ListNode(1)

        return result.next