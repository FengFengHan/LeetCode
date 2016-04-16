# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node == None:
            return None
        graphNodes = {}
        cloneNode = self.getGraphNode(node,graphNodes)
        return cloneNode
    def getGraphNode(self,node,graphNodes):
        cloneNode = UndirectedGraphNode(node.label)
        graphNodes[cloneNode.label] = cloneNode
        for neighborNode in node.neighbors:
            if neighborNode.label in graphNodes:
                cloneNeighrNode = graphNodes(neighborNode.label)
            else:
                cloneNeighrNode = self.getGraphNode(neighborNode,graphNodes)
            cloneNode.neighbors.append(cloneNeighrNode)
        return cloneNode

