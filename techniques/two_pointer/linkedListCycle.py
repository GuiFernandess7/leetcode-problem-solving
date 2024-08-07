# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head.next

    while (fast is not None) and (fast.next is not None):
        if slow == fast:
            return True

        slow = slow.next
        fast = fast.next.next

    return False

if __name__=="__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)

    print(hasCycle(l1))