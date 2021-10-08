from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}


def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    list = []
    try:
        cur = l1
        while True:
            list.append(cur.val)
            if cur.next is None:
                break
            cur = cur.next
    except AttributeError:
        pass

    try:
        cur = l2
        while True:
            list.append(cur.val)
            if cur.next is None:
                break
            cur = cur.next
    except AttributeError:
        pass
    list.sort()
    try:
        rlt = ListNode(list[0])
    except IndexError:
        return None
    cur = rlt
    for i in list:
        cur.next = ListNode(i)
        cur = cur.next
    rlt = rlt.next
    return rlt
