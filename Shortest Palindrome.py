class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        # Manacher Algorithm
        p = [1] * (2*len(s) + 1)
        insertChar = "@"
        newS = insertChar + insertChar.join(s) + insertChar
        id,mx = 0,0
        maxLen = 1
        for i in range(len(newS)):
            if mx > i:
                p[i] = min(p[2 * id - i], mx - i)
            while i + p[i] < len(newS) and i - p[i] >= 0 and newS[i + p[i]] == newS[i - p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                id = i
                mx = i + p[i]
            if p[i] == i +1 and p[i] - 1 > maxLen:
                maxLen = p[i] - 1

        res = s[len(s)-1:maxLen-1:-1] + s
        return res
x = "aba"
s = Solution()
ans = s.shortestPalindrome(x)


