# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tempo = head
        n = 0

        while tempo:
            n += 1
            tempo = tempo.next

        ptr = head
        prev = head

        for i in range(n-k-1):
            prev = prev.next

        if k == n:
            return head.next
        if k == 1:
            prev.next = None
        else:
            prev.next = prev.next.next

        return head