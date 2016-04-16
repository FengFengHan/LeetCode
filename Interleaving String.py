class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        # dp = [[False] * (len(s2) + 1)]*(len(s1) + 1)  #it not work
        # dp[i][j]: if s1[0:i] and s2[0:j] can form s3[0:i+j]
        dp = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(len(s1)):
            if s1[i] == s3[i]:
                dp[i+1][0] = True
            else:
                break
        for j in range(len(s2)):
            if s2[j] == s3[j]:
                dp[0][j+1] = True
            else:
                break
        for i in range(len(s1)):
            for j in range(len(s2)):
                if ((s1[i] == s3[i+j+1] and dp[i][j+1]) or (s2[j] == s3[i+j+1] and dp[i+1][j])):
                    dp[i+1][j+1] = True
        return dp[len(s1)][len(s2)]

s1,s2,s3 = "a","","c"
s = Solution()
ans = s.isInterleave(s1,s2,s3)


