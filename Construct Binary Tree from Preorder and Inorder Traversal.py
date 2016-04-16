# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        value = preorder[0]
        tree = TreeNode(value)
        pos = 0
        while inorder[pos] != value:
            pos += 1
        tree.left = self.buildTree(preorder[1:pos + 1],inorder[0:pos])
        tree.right = self.buildTree(preorder[pos+1:],inorder[pos + 1:])
        return tree
        
        