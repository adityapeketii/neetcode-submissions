# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergetwo(l1, l2):
            mainptr = ListNode()
            ptr = mainptr

            while l1 and l2:
                if l1.val <= l2.val:
                    ptr.next = l1
                    l1 = l1.next
                elif l1.val > l2.val:
                    ptr.next = l2
                    l2 = l2.next
                ptr = ptr.next

            if l1:
                ptr.next = l1
            elif l2:
                ptr.next = l2

            return mainptr.next

        if len(lists) == 0 or lists is None:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(mergetwo(l1, l2))
            lists = merged

        return lists[0]


