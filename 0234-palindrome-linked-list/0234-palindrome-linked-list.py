# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = self.splitLL(head)
        slow = self.reverseLL(slow)

        while (slow is not None) and (slow.val == head.val):
            head = head.next
            slow = slow.next
        return slow is None
        
    def reverseLL(self,temp):
        prev,curr = None,temp
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def splitLL(self,head):
        slow, fast = head,head

        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next 

        return slow
    