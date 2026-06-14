# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2

        ret = ListNode(1)
        cret = ret

        while c1 != None or c2 != None:
            if c1 == None:
                cret.next = ListNode(c2.val)
                c2 = c2.next
            elif c2 == None:
                cret.next = ListNode(c1.val)
                c1 = c1.next
            else:
                if c1.val >= c2.val:
                    cret.next = ListNode(c2.val)
                    c2 = c2.next
                else:
                    cret.next = ListNode(c1.val)
                    c1 = c1.next

            cret = cret.next

        return ret.next
