# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head
        cur_pre = res.next
        if cur_pre is not None:
            cur = cur_pre.next
        else:
            cur = None
        cur_ind = 2
        while cur is not None:
            cur_next = cur.next
            pointer_pre = res
            pointer = res.next
            pointer_ind = 1
            # 如果对于这种情况不进行单独判断，而是直接从头开始，会超时而通不过
            if  cur.val >= cur_pre.val:
                cur_pre = cur
            else:
                while pointer_ind < cur_ind:
                    if pointer.val > cur.val:
                        cur_pre.next = cur.next
                        cur.next = pointer
                        pointer_pre.next = cur
                        break
                    pointer_pre = pointer
                    pointer = pointer.next
                    pointer_ind += 1
            cur = cur_next
            cur_ind += 1
        return res.next






