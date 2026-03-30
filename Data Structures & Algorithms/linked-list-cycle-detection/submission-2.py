# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        unique_nodes = set()

        while current:
            if current in unique_nodes:
                return True

            unique_nodes.add(current)

            current = current.next

        return False

