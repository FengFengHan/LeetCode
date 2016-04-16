class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = self.generateParenthesisHelp(n,n)
        for i in  range(len(res)):
            for j in range(0,len(res[i]),2):
                res[i][j] = "("*res[i][j]
                res[i][j+1] = ")"*res[i][j+1]
            res[i] = "".join(res[i])
        return res

    def generateParenthesisHelp(self,lnum,rnum):
        res = []
        res.append([lnum,rnum])
        more = rnum - lnum
        for i in range(1,lnum):
            for j in range(1,more + i +1):
                tmp = [i,j]
                subRes = self.generateParenthesisHelp(lnum-i,rnum-j)
                for k in range(len(subRes)):
                    res.append(tmp + subRes[k])
        return res


