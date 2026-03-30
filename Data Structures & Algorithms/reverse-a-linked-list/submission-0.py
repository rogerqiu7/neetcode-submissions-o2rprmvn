# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None

        while current:
            # set next node as the one after current
            # next_node = 1.next = 2
            next_node = current.next
            # update currents next to previous
            # 1.next = None
            current.next = previous
            # update previous to current
            # previous = 1
            previous = current
            # set current as the next one
            # current = 2
            current = next_node

        return previous