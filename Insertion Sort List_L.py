# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None or head.next == None:
            return head

        node = head;

        while node.next != None:
            cur = node.next

            if cur.val >= node.val:
                node = node.next
                continue

            node.next = cur.next

            if cur.val <= head.val:
                cur.next = head
                head = cur
                continue

            pos = self.findInsertPos(head, cur)

            cur.next = pos.next
            pos.next = cur

        return head


    def findInsertPos(self, head, node):
        pos = head
        while head != None and node.val > head.val:
            pos = head
            head = head.next

        return pos