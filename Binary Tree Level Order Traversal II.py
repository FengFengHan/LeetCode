# class TreeNode(object):
# def __init__(self, x):
#     self.val = x
#     self.left = None
#     self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root == None:
            return result
        nextLayer = []
        nextLayer.append(root)
        while len(nextLayer) > 0:
            result.append(nextLayer)
            nextLayer = []
            for father in result[-1]:
                if father.left != None:
                    nextLayer.append(father.left)
                if father.right != None:
                    nextLayer.append(father.right)
        result = [[node.val for node in layer] for layer in result]
        for i in range(len(result)//2):
            sym_i = len(result) - 1 - i
            result[i],result[sym_i] = result[sym_i], result[i]
        return result
