# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.isBST(root,None,None)

    def isBST(self,root,lParentVal,rParentVal):
        if root == None:
            return True
        if self.isValidRoot(root,lParentVal,rParentVal) and self.isBST(root.left,root.val,rParentVal) and self.isBST(root.right, lParentVal, root.val) :
            return True
        return False

    def isValidRoot(self,root,lParentVal,rParentVal):
        if lParentVal != None and root.val >= lParentVal:
            return False
        if rParentVal != None and root.val <= rParentVal:
            return False
        return True



