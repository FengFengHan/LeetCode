class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def createTree(lists, s = 0):
    if s >= len(lists) or lists[s] == None:
        return None
    else:
       tree = TreeNode(lists[s])
       tree.left = createTree(lists, 2*s + 1)
       tree.right = createTree(lists, 2*s + 2)
    return tree