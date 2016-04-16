# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.w1 = None
        self.w2 = None
        self.inorder(root)
        self.w1.val, self.w2.val = self.w2.val, self.w1.val

    def inorder(self,root):
        pre = None
        while root != None:
            if root.left == None:
                if pre != None and pre.val > root.val:
                    if self.w1 is None:
                        self.w1, self.w2 = pre,root
                    else:
                        self.w2 = root
                pre = root
                root = root.right
            else:
                tmp = root.left
                while tmp.right != None and tmp.right != root:
                    tmp = tmp.right
                if tmp.right == None:
                    tmp.right = root
                    root = root.left
                else:
                    tmp.right = None # without changing its structure
                    if pre != None and pre.val > root.val:
                        if self.w1 is None:
                            self.w1, self.w2 = pre,root
                        else:
                            self.w2 = root
                    pre = root
                    root = root.right

x = TreeNode(0)
t = TreeNode(1)
x.left = t
s = Solution.recoverTree(x)


