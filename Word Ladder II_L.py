class Solution:
    # @param start, a set of string
    # @return two dictionaries
    def _buildSig(self, contents):
        sig = {}    # Records the signatures for each string
        bucket = {} # Records the strings with each signature
        
        for string in contents:
            sig[string] = []
            for index in xrange(len(string)):
                tempSig = string[:index] + "*" + string[index+1:]
                sig[string].append(tempSig)
                
                if tempSig not in bucket:   bucket[tempSig] = []
                bucket[tempSig].append(string)
        
        return sig, bucket
    
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        # Build the graph.
        # Two nodes (whose value is the string in dict), are connected if
        # they have one same signature or more.
        sig, bucket = self._buildSig(set([start, end]) | dict)
 
        result = []
        
        accessed = {}
        for string in dict:     accessed[string] = False
        accessed[start] = True
        
        # Travel the graph in breadth-first search.
        currentLayer = [[start]]
        steps = 1
        while len(currentLayer) != 0 and len(result) == 0:
            steps += 1
 
            nextLayer = []
            accessedTemp = []
            for intermediate in currentLayer:
                signatures = sig[intermediate[-1]]
                for signature in signatures:
                    for nextLayerCandidate in bucket[signature]:
                        # Transformation from start to end finished.
                        if nextLayerCandidate == end:
                            result.append(intermediate + [end])
                            continue
                        
                        # Accessed before. Not to access again.
                        if accessed[nextLayerCandidate]:
                            continue
                        
                        # We cannot set the accessed flag instantly here.
                        # The other same-deep nodes(stirng) also have the 
                        # right to jump to this node(string).
                        accessedTemp.append(nextLayerCandidate)
                        nextLayer.append(intermediate + [nextLayerCandidate])
            
            for item in accessedTemp:   accessed[item] = True      
            currentLayer = nextLayer
        
        return result