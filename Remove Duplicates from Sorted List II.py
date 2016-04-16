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
        res = ListNode(0)
        res.next = head
        node = res
        while node.next is not None:
            cur = node.next
            if cur.next is None or cur.val != cur.next.val:
                node = cur
                continue
            else:
               value = cur.val
               cur = cur.next
               while cur != None and cur.val == value:
                   cur = cur.next
               node.next = cur
        return res.next
