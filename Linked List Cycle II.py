# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        #�ж��Ƿ���Ȧ
        slow, fast = head,head.next
        while slow != fast:
            if fast == None:
                return None
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next
            else:
                return None
        #��ͷ���غϴ��ֱ����
        start,meet = head,slow.next
        while start != meet:
            start = start.next
            meet = meet.next
        return start