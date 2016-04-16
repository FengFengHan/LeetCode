# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = head
        while res is not None:
            value = res.val
            cur = res.next
            while cur is not None and cur.val == value:
                cur = cur.next
            res.next = cur
            res = res.next
        return head