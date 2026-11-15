# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return False
        i = j = head
        while i != None and j != None:
            i = i.next
            if j.next != None:
                j = j.next.next
            else:
                return False
            if i == j:
                return True
        return False