# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(0)
        new = new_head
        while l1 and l2:
            if l1.val <= l2.val:
                new.next = ListNode(l1.val)
                l1 = l1.next
                new = new.next
            else:
                new.next = ListNode(l2.val)
                l2 = l2.next
                new = new.next
        if l1:
            new.next = l1
        else:
            new.next = l2
        return new_head.next


if __name__ == '__main__':
    s= Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    s.mergeTwoLists(l1,l2)
