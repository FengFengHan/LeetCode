class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i, j = 0,0
        while i < len(haystack):
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                i += 1
                j += 1
            i = i - j + 2
            if j == len(needle):return  i
            j = 0
        return -1
