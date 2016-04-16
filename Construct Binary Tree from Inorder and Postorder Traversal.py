# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder = inorder
        self.postorder = postorder
        self.inPos = {}
        for i in range(len(inorder)):
            self.inPos[inorder[i]] = i
        return self.createTree(0,len(inorder)-1,0,len(postorder)-1)
    def createTree(self,inBeg,inEnd,posBeg,posEnd):
        if inBeg > inEnd:
            return None
        value = self.postorder[posEnd]
        tree = TreeNode(value)
        pos = self.inPos[value]
        tree.left = self.createTree(inBeg,pos-1,posBeg,posBeg + pos - 1 - inBeg)
        tree.right = self.createTree(pos + 1, inEnd,posBeg + pos - inBeg,posEnd-1)
        return tree


