# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        greatehead, lesshead = ListNode(0), ListNode(0)
        cur, lesscur= greatehead,lesshead
        while head != None:
            if head.val >= x:
                cur.next = head
                cur = cur.next
            else:
                lesscur.next = head
                lesscur = lesscur.next
            head = head.next
        cur.next = None
        lesscur.next = greatehead.next
        return lesshead.next