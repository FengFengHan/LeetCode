class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        sig, bucket = self.buildGraph(set([beginWord,endWord])|wordlist)
        curLayer = [[beginWord]]
        result = []
        accessedword = {}
        for word in wordlist:
            accessedword[word] = False
        while len(curLayer) > 0 and len(result) == 0:
            nextLayer = []
            for intermediate in curLayer:
                accessedword[intermediate[-1]] = True
            for intermediate in curLayer:
                signatures = sig[intermediate[-1]]
                for signature in signatures:
                    for nextLayerWord in bucket[signature]:
                        if nextLayerWord == endWord:
                            result.append(intermediate + [endWord])
                            continue
                        if accessedword[nextLayerWord]:
                            continue
                        nextLayer.append(intermediate + [nextLayerWord])
            curLayer = nextLayer
        return result

    def buildGraph(self,words):
        sig = {}
        bucket = {}
        for word in words:
            sig[word] = []
            for m in range(len(word)):
                tmpSig = word[0:m] + "*" + word[m+1:]
                sig[word].append(tmpSig)
                if bucket.get(tmpSig,None) == None:
                    bucket[tmpSig] = []
                bucket[tmpSig].append(word)
        return sig,bucket

beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog"]
s = Solution()
ans =s.findLadders(beginWord,endWord,wordList)
