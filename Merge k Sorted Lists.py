# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = ListNode(0)
        head = res
        self.heap = [[i, lists[i].val] for i in range(len(lists)) if lists[i] is not None]
        self.hsize = len(self.heap)
        # if i > self.hsize//2, then i is a terminal node that is not modified
        for i in  range( self.hsize//2 -1, -1, -1):
            self.adjustdown(i)
        while self.hsize > 1:
            pos = self.heap[0][0]
            res.next = lists[pos]
            lists[pos] = lists[pos].next
            res = res.next
            if lists[pos] is not None:
                self.heap[0][1] = lists[pos].val
            else:
                self.heap[0] = self.heap[self.hsize - 1]
                self.hsize -= 1
            self.adjustdown(0)
        if self.hsize > 0:
            res.next = lists[self.heap[0][0]]
        return head.next
    #
    def adjustdown(self, p):
        l = 2*p + 1
        r = 2*p + 2
        np = p
        if l >= self.hsize:
            return
        elif r >= self.hsize:
            if self.heap[l][1] < self.heap[p][1]:
                np = l
        else:
            if self.heap[l][1] < self.heap[p][1] and self.heap[l][1] <= self.heap[r][1]:
                np = l
            elif self.heap[r][1] < self.heap[p][1] and self.heap[r][1] <= self.heap[l][1]:
                np = r
        if np != p:
            self.heap[p], self.heap[np] = self.heap[np], self.heap[p] # swap value!
            self.adjustdown(np)
    #a more elegant method: (1) 如果变量只是不断更新而不用回退的话，可以用迭代，迭代往往比递归更快 （2）对于左右与当前值的比较替换更优雅
    def adjustdown(self, p):
        lc = lambda x: (x + 1) * 2 - 1
        rc = lambda x: (x + 1) * 2
        while True:
            np, pv = p, self.heap[p][1]
            if lc(p) < self.hsize and self.heap[lc(p)][1] < pv:
                np, pv = lc(p), self.heap[lc(p)][1]
            if rc(p) < self.hsize and self.heap[rc(p)][1] < pv:
                np = rc(p)
            if np == p:
                break
            else:
                self.heap[np], self.heap[p] = self.heap[p], self.heap[np]
                p = np
    #

# test case:
# x = [[1,2,2],[1,1,2]]
# x_LN = []
# for i in range(len(x)):
#     tmp = ListNode(0)
#     head = tmp
#     for j in range(len(x[i])):
#         tmp.next = ListNode(x[i][j])
#         tmp = tmp.next
#     x_LN.append(head.next)
# s = Solution()
# t = s.mergeKLists(x_LN)

