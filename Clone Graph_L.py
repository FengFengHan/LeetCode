# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # Empty graph
        if node == None:                        return

        # Do the work in two rounds. In the first round, we clone all the
        # new nodes only with label. And let their neighbors array empty.
        # In the second round, we will assign the neighbors of cloned
        # node with the reference to new cloned ones.

        # Clone nodes only with label
        cloned = {}
        currentLayer = [node]

        while len(currentLayer) != 0:
            nextLayer = []

            for toClone in currentLayer:
                if toClone in cloned:       continue

                temp = UndirectedGraphNode(toClone.label)
                nextLayer.extend(toClone.neighbors)

                cloned[toClone] = temp

            currentLayer = nextLayer

        # Assign the neighbors of new cloned nodes.
        for oldNode in cloned:
            newNode = cloned[oldNode]
            newNode.neighbors = [cloned[neighbor] for neighbor
                                                  in oldNode.neighbors]

        return cloned[node]