# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0)
        answer = newHead
        if not head or not head.next:
            return head
        while head and head.next:
            newHead.next = ListNode(head.next.val, ListNode(head.val, head.next.next))
            head = head.next.next
            newHead = newHead.next.next
        return answer.next