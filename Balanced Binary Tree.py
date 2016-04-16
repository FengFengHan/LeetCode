# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.balhei(root)[0]
    # def depth(self,root):
    #     if root is None:
    #         return 0
    #     return max(self.depth(root.left),self.depth(root.right)) + 1
    def balhei(self,root):
        if root is None:
            return (True,0)
        l = self.balhei(root.left)
        if not l[0]:
            return (False,-1)
        r = self.balhei(root.right)
        if not r[0]:
            return (False,-1)
        ld = l[1]
        rd = r[1]
        if abs(ld -rd) > 1:
            return (False,-1)
        d = max(ld,rd) + 1
        return (True,d)




