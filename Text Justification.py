class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return [" "] * maxWidth
        res = []
        line = []
        lens = 0
        for word in words:
            sepSpaceNum = 0 if len(line) < 1 else len(line)
            if lens + len(word) + sepSpaceNum > maxWidth:
                res.append(self.addSpaces(line,lens,maxWidth))
                del line[:]
                lens = len(word)
            else:
                lens += len(word)
            line.append(word)
        #alone process last line
        lastLine = line[0]
        for i in range(1,len(line)):
            lastLine = lastLine + " " + line[i]
        lastLine = lastLine + " " * (maxWidth - len(lastLine))
        res.append(lastLine)
        return res

    def addSpaces(self, words,lens, width):
        wordNum = len(words)
        if wordNum == 1:
            return words[0] + " "*(width - lens)
        spaceNum = (width - lens)//(wordNum -1)
        moreSpaceNum = (width - lens) % (wordNum - 1)
        spaces = " "*spaceNum
        moreSpaces = spaces + " "
        res = ""
        for i in range(len(words)-1):
            if i < moreSpaceNum:
                res = res + words[i] + moreSpaces
            else:
                res = res + words[i] + spaces
        res = res + words[len(words) - 1]
        return res







