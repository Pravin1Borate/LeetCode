# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        
        if not head:
            return 

        result = []
        while head is not None:
            result.append(head.val)
            head = head.next

        # print(result)
        result[k-1],result[-k] = result[-k],result[k-1]
        # print(result)
        temp = ListNode(result[0])
        head = temp
        for val in result[1:]:
            temp.next = ListNode(val)
            temp = temp.next
        return head
