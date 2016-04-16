# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class IndexedNode(object):
    def __init__(self,index,node):
        self.ind = index
        self.nod = node

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # for every node, get index and val
        index2val = {}
        tree = []
        if root != None:
            tree.append(IndexedNode(0,root))
        while len(tree) > 0:
            indexedNode = tree.pop(0)
            index = indexedNode.ind
            node = indexedNode.nod
            index2val[index] = node.val
            if node.left != None:
                tree.append(IndexedNode(index * 2 + 1, node.left))
            if node.right != None:
                tree.append(IndexedNode(index * 2 + 2, node.right))
        # map to string
        res = ""
        for key in index2val.keys():
            res += (str(key) + "," + str(index2val[key]) + ",")
        if res != "":
            res = res[:-1]
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        #string to map
        indAndVal = data.split(",")
        index2val = {}
        i = 0
        while i < len(indAndVal):
            index = int(indAndVal[i])
            val = indAndVal[i+1]
            index2val[index] = val
            i += 2
        # build tree by the map index2val
        root = self.buildTree(0,index2val)
        return root

    def buildTree(self,index, index2val):
        if (index2val.get(index,None) == None):
            return None
        else:
            tree = TreeNode(index2val[index])
            tree.left = self.buildTree(2*index + 1, index2val)
            tree.right = self.buildTree(2*index + 2, index2val)
            return tree

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))