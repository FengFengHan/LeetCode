# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        nodes = [] #记录所有节点
        while head != None:
            nodes.append(head)
            head = head.next
        if len(nodes) == 0:
            return []
        k = k % len(nodes)
        if len(nodes) == k or k == 0:
            return nodes[0]
        res = nodes[len(nodes) - k]
        nodes[len(nodes) - 1].next = nodes[0]
        nodes[len(nodes) - k -1].next = None
        return res

