# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        ltor = True
        curLayer = [root]
        while len(curLayer) > 0:
            res.append(curLayer)
            nextLayer = []
            ltor = not ltor
            curLayer_re = curLayer[::-1]
            if ltor:
                for node in curLayer_re:
                    if node.left != None:
                        nextLayer.append(node.left)
                    if node.right != None:
                        nextLayer.append(node.right)
            else:
                for node in curLayer_re:
                    if node.right != None:
                        nextLayer.append(node.right)
                    if node.left != None:
                        nextLayer.append(node.left)
            curLayer = nextLayer
        res = [[node.val for node in layer] for layer in res]
        return res



