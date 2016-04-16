class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0 or len(word2) == 0:
            return abs(len(word1) - len(word2))
        elif word1 == word2:
            return 0
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:],word2[1:])
        else:
            # insert
            insertStep = 0
            while insertStep < len(word2) and word2[insertStep] != word1[0]:
                insertStep += 1
            insertStep = insertStep + self.minDistance(word1[0:],word2[insertStep:])
            #delete
            deleteStep = 0
            while deleteStep < len(word1) and word1[deleteStep] != word2[0]:
                deleteStep += 1
            deleteStep = deleteStep + self.minDistance(word1[deleteStep:],word2[0:])
            # replace
            replaceStep = 1 + self.minDistance(word1[1:],word2[1:])
            step = min([insertStep,deleteStep,replaceStep])
            return step
