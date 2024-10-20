# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        vec = []
        p = []

        while head:
            vec.append(head.val)
            head = head.next
        
        if not vec:
            return None

        for key,val in enumerate(vec[::-1]):
            if (key+1) != n:
                p.append(val)
        print(p)
        if not p:
            return None

        temp = ListNode(p[-1])
        head = temp

        for i in p[::-1][1:]:
            temp.next = ListNode(i)
            temp = temp.next
        return head

        