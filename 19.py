# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        answer = head
        left = answer
        for i in range(n):
            head = head.next
        right = left.next
        while True:
            if head == None:
                break
            last = left
            head = head.next
            right = right.next
            left = left.next
        if right:
            left.val = right.val
            left.next = right.next
        else:
            last.next = None
        return answer
