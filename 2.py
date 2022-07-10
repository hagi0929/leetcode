class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        result_tail = result
        nexts = 0

        while l1 or l2 or nexts:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            temp = nexts
            nexts = (num1 + num2 + temp) // 10
            val = (num1 + num2 + temp) % 10
            result_tail.next = ListNode(val)
            result_tail = result_tail.next

            if l1:
                l1 = l1.next if l1.next else None
            if l2:
                l2 = l2.next if l2.next else None

        return result.next