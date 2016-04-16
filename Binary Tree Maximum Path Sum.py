# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = root.val
        self.subSum(root)
        return self.max


    def subSum(self, root):
        if root == None:
            return 0
        left = self.subSum(root.left)
        right = self.subSum(root.right)
        if left < 0:
            left = 0
        if right < 0:
            right = 0
        subPathSum = root.val + max(left,right)
        pathSum = root.val + left + right
        if pathSum > self.max:
            self.max = pathSum
        return subPathSum

