class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        # Manacher Algorithm
        insertChar = "#"
        s1 = insertChar + insertChar.join(s) + insertChar
        p = [1] * (2*len(s) +1)
        id,mx = 0,0
        max_id,max_len = 1,1
        for i in range(len(s1)):
            if mx > i:
                p[i] = min(mx - i, p[2*id - i])
            while i + p[i] < len(s1) and i - p[i] >= 0 and s1[i+p[i]] == s1[i-p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                mx = i + p[i]
                id = i
            if p[i] - 1 > max_len:
                max_len = p[i] - 1
                max_id = i
        #restore to original string
        idInS = (max_id + 1)//2 - 1
        leftLen = (max_len - 1)//2
        rightLen = max_len - 1 - leftLen
        res = s[idInS-leftLen:idInS+rightLen +1]
        return res
x = "bb"
s= Solution()
ans  = s.longestPalindrome(x)
