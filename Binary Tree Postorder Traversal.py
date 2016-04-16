# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        head = TreeNode(-1)
        head.left = root
        cur = head
        while(cur != None):
            if(cur.left == None):
                cur = cur.right
            else:
                pre = cur
                node = cur.left
                while(node != None and node != cur):
                    pre = node
                    node = node.right
                if(node == None):
                    pre.right = cur
                    cur = cur.left
                else:
                    res.extend(self.reverseVisit(cur.left,node))
                    cur = cur.right
        return res

    def reverseVisit(self,start,end):
        res = []
        rStart = self.reverse_(start,end)
        node = rStart
        while(node != end):
            res.append(node.val)
            node = node.right
        self.reverse_(rStart,end)
        return res


    def reverse_(self,start,end):
        pre = end
        cur = start
        while(cur != end):
            next_ = cur.right
            cur.right = pre
            pre = cur
            cur = next_
        return pre
