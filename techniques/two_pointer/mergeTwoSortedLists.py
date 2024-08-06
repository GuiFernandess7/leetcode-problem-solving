class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_linked_list(l1, l2):
    placeholder = ListNode()
    tail = placeholder

    l1_pointer = l1
    l2_pointer = l2

    while l1_pointer and l2_pointer:
        if l1_pointer.val < l2_pointer.val:
            tail.next = l1_pointer
            l1_pointer = l1_pointer.next
        else:
            tail.next = l2_pointer
            l2_pointer = l2_pointer.next

        tail = tail.next

    if l1_pointer:
        tail.next = l1_pointer
    elif l2_pointer:
        tail.next = l2_pointer

    return placeholder.next


if __name__=="__main__":
    # l1 = [1, 2, 4] l2 = [1, 3, 4]
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    mergedList = merge_two_linked_list(l1, l2)
    node = mergedList

    while node:
        print(node.val)
        node = node.next
