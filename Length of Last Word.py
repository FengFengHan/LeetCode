class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastWord = []
        i = len(s) - 1
        while i >= 0:
            while i >= 0 and s[i].isspace():
                i -= 1
            if i < 0:
                break;
            isWord = True
            while i >= 0 and not s[i].isspace():
                if not s[i].isalpha():
                    isWord = False
                    lastWord = []
                if isWord:
                    lastWord.append(s[i])
                i -= 1
            if isWord: break
        return len(lastWord)