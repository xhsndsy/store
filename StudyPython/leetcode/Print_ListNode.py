# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) :
        List = []
        while head:
            List.append(head.val)
            head = head.next
        return List[::-1]
