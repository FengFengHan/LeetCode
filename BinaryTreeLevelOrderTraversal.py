# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        nodes = []
        if root is not None:
            nodes.append(root)
        while len(nodes) > 0:
            tmp = []
            next_nodes = []
            for node in nodes:
                tmp.append(node.val)
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            res.append(tmp)
            nodes = next_nodes
        return res
