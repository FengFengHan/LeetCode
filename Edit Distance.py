class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0 or len(word2) == 0:
            return abs(len(word1) - len(word2))
        # D = [[0] * (len(word2)+1)]* (len(word1) + 1) # it does not work
        D = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        #initialize
        for i in range(len(word1)+1):
            D[i][0] = i
        for j in range(len(word2)+1):
            D[0][j] = j
        #DP
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                D[i][j] = min(D[i-1][j-1] + (1 if word1[i-1] != word2[j-1] else 0), D[i-1][j] + 1, D[i][j-1] + 1)
        return D[len(word1)][len(word2)]

word1 = "ab"
word2 = "bc"
s = Solution()
ans = s.minDistance(word1,word2)