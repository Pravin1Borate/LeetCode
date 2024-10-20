# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vec = []

        while head:
            vec.append(head.val)
            head = head.next
        vec = sorted(list(set(vec)))
    
        if not vec:
            return None

        print(vec)

        temp = ListNode(vec[0])
        head = temp
        for p in vec[1:]:
            temp.next = ListNode(p)
            temp = temp.next
        return head


        