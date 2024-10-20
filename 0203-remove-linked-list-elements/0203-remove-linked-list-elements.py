# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        vec  = []
        p = []
        while head:
            vec.append(head.val)
            head = head.next
        
        if not vec:
            return None
        
        for i in vec:
            if i != val:
                p.append(i)
        if not p:
            return None

        temp = ListNode(p[0])
        head = temp
        for i in p[1:]:
            temp.next = ListNode(i)
            temp = temp.next
        return head
        
        return head
        