class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        res = strs[0]
        for i in range(1,len(strs)):
            str = strs[i]
            j = 0
            while j < len(res) and j < len(str) and res[j] == str[j]:
                j += 1
            res = res[:j]
        return res
