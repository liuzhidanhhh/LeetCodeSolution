# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        length = 1
        res_head = head
        cur_p = head
        while cur_p.next:
            if length < k:
                cur_p = cur_p.next
                length += 1
            else:
                res_head = res_head.next
                cur_p = cur_p.next
        return res_head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    a = Solution()
    a.getKthFromEnd(head, 2)
