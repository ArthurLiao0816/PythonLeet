class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=None)
        pointer = dummy
        s1 = s2 = ''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        s1 = s1[::-1]
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        s2 = s2[::-1]
        rlt = str(int(s1)+int(s2))[::-1]
        for c in rlt:
            pointer.next = ListNode(val=int(c))
            pointer = pointer.next
        return dummy.next
