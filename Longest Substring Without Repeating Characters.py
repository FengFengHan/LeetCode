class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        start = 0
        charToInd = {}
        for char in set(s):
            charToInd[char] = -1
        for i in range(len(s)):
            if charToInd[s[i]] == -1:
                charToInd[s[i]] =  i
            else:
                newStart = charToInd[s[i]] + 1
                if i - start > maxLen:
                    maxLen = i - start
                for j in range(start,newStart):
                    charToInd[s[j]] = -1
                start = newStart
                charToInd[s[i]] = i
        if len(s) - start > maxLen: maxLen = len(s) - start
        return maxLen

x = "abba"
s = Solution()
ans = s.lengthOfLongestSubstring(x)