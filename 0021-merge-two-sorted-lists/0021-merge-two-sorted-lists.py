# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        vec = []

        while list1:
            vec.append(list1.val)
            list1 = list1.next
        
        while list2:
            vec.append(list2.val)
            list2 = list2.next

        vec = sorted(vec)

        if not vec:
            return None


        temp = ListNode(vec[0])
        head = temp
        print(vec[1:])
        for p in vec[1:]:
            temp.next = ListNode(p)
            temp = temp.next
        return head



        