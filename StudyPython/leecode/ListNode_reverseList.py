# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur_head = head
        new_head = None

        while cur_head:
            next_head = cur_head.next
            cur_head.next = new_head
            new_head = cur_head
            cur_head = next_head

        return new_head