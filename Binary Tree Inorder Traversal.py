# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        node = root
        while node != None:
            if node.left == None:
                res.append(node.val)
                node = node.right
            else:
                tmp = node.left
                while tmp.right != None and tmp.right != node:
                    tmp = tmp.right
                if tmp.right == None:
                    tmp.right = node
                    node = node.left
                # the node had been visited
                else:
                    res.append(node.val)
                    node = node.right
        return res

