# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res = self.generateSubTrees(1,n)
        return res

    def  generateSubTrees(self,start,end):
        if start > end:
            return [None]
        trees = []
        for root in range(start,end + 1):
            lTrees = self.generateSubTrees(start,root-1)
            rTrees = self.generateSubTrees(root+1,end)
            for lTree in lTrees:
                for rTree in rTrees:
                    tree = TreeNode(root)
                    tree.left = lTree
                    tree.right = rTree
                    trees.append(tree)
        return trees



