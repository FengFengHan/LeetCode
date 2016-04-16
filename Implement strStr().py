class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        res = self.KMP(haystack,needle,0)
        return  res

    def KMP(self,s,t,pos):
        i = pos
        j = 0
        next = self.get_next(t)
        while i < len(s) and j < len(t):
            if( j == -1 or s[i] == t[j]):
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(t):
            return i - j
        return -1

    def get_next(self,t):
        next = [-1] * len(t)
        j = -1
        i = 0
        next[i] = j
        while i < len(t) -1:
            if j == -1 or t[i] == t[j]:
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]
        return next





