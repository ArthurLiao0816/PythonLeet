class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def recursion(a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a.val <= b.val:
            a.next = recursion(a.next, b)
            return a
        else:
            b.next = recursion(a, b.next)
            return b
    return recursion(l1, l2)
