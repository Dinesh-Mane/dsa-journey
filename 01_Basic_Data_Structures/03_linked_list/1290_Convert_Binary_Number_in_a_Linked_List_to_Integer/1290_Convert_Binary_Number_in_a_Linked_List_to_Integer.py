# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        n = 0
        cur = head
        while cur:
            n = (n << 1) | cur.val
            cur = cur.next
        return n