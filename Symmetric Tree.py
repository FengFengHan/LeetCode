# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        curLayer = [root]
        while len(curLayer) > 0:
            if not self.isSymLayer(curLayer):
                return False
            nextLayer = []
            for node in curLayer:
                if node != None:
                    nextLayer.append(node.left)
                    nextLayer.append(node.right)
            curLayer = nextLayer
        return True
            
    def isSymLayer(self,layer):
        layer = [ node.val if node != None else node for node in layer]
        if len(layer) == 1:
            return True
        else:
            mid = (len(layer) + 1) //2
            if layer[0:mid] != layer[len(layer)-1:len(layer) - 1 - mid:-1]:
                return False
            return  True


def createTree(lists, s = 0):
    if s >= len(lists) or lists[s] == None:
        return None
    else:
       tree = TreeNode(lists[s])
       tree.left = createTree(lists, 2*s + 1)
       tree.right = createTree(lists, 2*s + 2)
    return tree
x = [1,2,2]
t2 = createTree(x)
s = Solution()
s.isSymmetric(t2)
        

