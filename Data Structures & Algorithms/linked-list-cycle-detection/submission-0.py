# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        visited = set()
        c = head
        while c != None:
            if c in visited:
                return True
            visited.add(c)
            c = c.next

        return False
        