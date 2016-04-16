class Solution(object):
    # As only dp[i-1][j-1] and dp[i][j-2] be used, 2 dimension dp[i][j] can be replaced by two 1 dimension list
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #intailize
        dp = [ [False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True
        # p = 'a*b*c*'
        for j in range(2,len(p)+1):
            if p[j-1] == '*':
                if dp[0][j-2] or (p[j-2] == '*' and dp[0][j-1]):
                    dp[0][j] = True
            if not dp[0][j-1] and not dp[0][j]:
                break

        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] != '*':
                    if (p[j-1]== '.' or s[i-1] == p[j-1]) and dp[i-1][j-1]:
                        dp[i][j] = True
                else:
                    matchStar = False
                    if(j >= 2 and dp[i][j-2]):
                        matchStar = True
                    else:
                        # notice the wrong method as follows:
                        # starCount = 1
                        # while starCount <= i and (p[j-2] == "." or s[i-starCount] == p[j-2]):
                        #     if(dp[i-starCount][j-2]):
                        #         matchStar = True
                        #         break
                        #     starCount += 1
                        if(p[j-2] == '.' or s[i-1] == p[j-2]) and dp[i-1][j]:
                            matchStar = True
                    dp[i][j] = matchStar

                #below is wrong, such as: s= 'aa' and p = 'aa'
                # if not dp[i][j] and (j < len(p) and p[j] != '*'):
                #     break
        return dp[len(s)][len(p)]



