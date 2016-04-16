# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param inOrderZone, an array to limit the nodes for current subtree
    #            inOrderZone[0] is the beginning position of current subtree
    #            in inorder array. inOrderZone[1] is the end position.
    # @param inPos, a dictionary with the position of each char in inorder.
    # @param preorder, a list of integers
    # @param preOrderZone, an array to limit the nodes for current subtree.
    #            Same as inOrderZone.
    # @param prePos, a dictionary with the position of each char in preorder.
    # @return a tree node
    def buildTreeHelper(self, inorder, inOrderZone, inPos, 
                              preorder, preOrderZone, prePos):
        ''' Built the tree recuisively. The first element in preOrderZone
            will always be the root of current tree (or subtree).
        '''
        # Reach the leaf.
        if inOrderZone[1] < inOrderZone[0] :           return None
        
        # Create the root node of current (sub)tree
        # The root node is in some middle place among inOrderZone.
        # The root node is in the first position of current preOrderZone.
        root = TreeNode(preorder[preOrderZone[0]])
        
        # Recursively build the left son of current root
        leftInOrderZone = [inOrderZone[0], inPos[root.val]-1]
        leftCount = inPos[root.val] - inOrderZone[0]
        leftPreOrderZone = [preOrderZone[0]+1, preOrderZone[0]+leftCount]
        root.left = self.buildTreeHelper(inorder, leftInOrderZone, inPos, 
                                         preorder, leftPreOrderZone, prePos)
        
        # Recursively build the right son of current root
        rightInOrderZone = [inPos[root.val]+1, inOrderZone[1]]
        rightCount = inOrderZone[1] - inPos[root.val]
        rightPreOrderZone = [preOrderZone[1]-rightCount+1, preOrderZone[1]]
        root.right = self.buildTreeHelper(inorder, rightInOrderZone, inPos, 
                                         preorder, rightPreOrderZone, prePos)
        
        return root
    
    # @param inorder, a list of integers
    # @param preorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        # There is not duplicate in the tree. And we record the position for
        # each charater in the inorder array and preorder array.
        inPos = {}
        prePos = {}
        for index in xrange(len(inorder)):
            inPos[inorder[index]] = index
            prePos[preorder[index]] = index
        
        return self.buildTreeHelper(inorder, [0, len(inorder)-1], inPos, 
                                    preorder, [0, len(preorder)-1], prePos)
    
        
        