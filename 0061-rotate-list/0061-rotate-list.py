# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = []
        temp = head
        while temp is not None:
            result.append(temp.val)
            temp = temp.next

        if not result:
            return

        result = self.rotateArray(result,k)

        temp = ListNode(result[0])
        name = temp
        for val in result[1:]:
            temp.next = ListNode(val)
            temp = temp.next
        return name
    
    def rotateArray(self,result,k):
        print(result)
        if (k == 0) or (k == len(result)):
            return result
        k = k % len(result)
        result[:] = result[-k:] + result[:-k]
        return result