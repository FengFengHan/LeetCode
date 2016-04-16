# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.mergeSort(head)

    def mergeSort(self,list_):
        if list_ is None or list_.next is None:
            return list_
        slow = list_
        fast = list_.next
        while fast is not None:
            fast = fast.next
            if fast is not None:
                slow = slow.next
                fast = fast.next
        mid = slow.next
        slow.next = None
        list_ = self.mergeSort(list_)
        mid = self.mergeSort(mid)
        return self.sortedMerge(list_,mid)

    def sortedMerge(self,list1, list2):
        res = ListNode(0)
        res_head = res
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
        if list1 is not None:
            res.next = list1
        elif list2 is not None:
            res.next = list2
        return res_head.next


