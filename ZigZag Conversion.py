class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = []
        maxLineNum = numRows if len(s) >= numRows else len(s)
        lines = [[] for i in range(maxLineNum)]
        for i in range(len(s)):
            lines[self.index2line(i,numRows)].append(s[i])
        for line in lines:
            res.extend(line)
        return "".join(res)

    def index2line(self,index,numRows):
        if numRows <= 2:
            patNum = numRows
        else:
            patNum = numRows + numRows - 2
        posInPat = index % patNum
        lineNum = posInPat if posInPat < numRows else patNum - posInPat
        return lineNum
