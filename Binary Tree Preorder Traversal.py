# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        node = root
        while node != None:
            result.append(node.val)
            if node.left == None:
                node = node.right
            else:
                tmp = node.left
                while tmp.right != None:
                    tmp = tmp.right
                tmp.right = node.right
                node = node.left
        return result