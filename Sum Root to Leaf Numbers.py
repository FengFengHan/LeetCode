# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.sum = 0
        nums = []
        self.dfs(root,nums)
        return self.sum

    def getSum(self,nums):
        res = nums[0]
        for i in range(1,len(nums)):
            res = res * 10 + nums[i]
        return res

    def dfs(self,root,nums):
        nums.append(root.val)
        if root.left == None and root.right == None:
            self.sum += self.getSum(nums)
            return
        if root.left != None:
            self.dfs(root.left,nums)
            nums.pop()
        if root.right != None:
            self.dfs(root.right,nums)
            nums.pop()

