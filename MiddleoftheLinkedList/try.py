from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        from math import ceil
        counter = 1
        pointer = head
        while pointer is not None:
            if pointer.next is None:
                break
            else:
                counter += 1
                pointer = pointer.next
        ans = head
        counter = ceil((counter-1)/2)
        while counter:
            ans = ans.next
            counter -= 1
        return ans
