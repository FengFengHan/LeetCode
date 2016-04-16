class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        numstr = ["1"]
        for _ in xrange(n-1):
            numstr = self.say(numstr)
        return "".join(numstr)


    def say(self,numstr):
        count = 0
        res = []
        for i in xrange(len(numstr)):
            if i < len(numstr) - 1 and numstr[i] == numstr[i+1]:
                count += 1
            else:
                count += 1
                res.append(str(count))
                res.append(numstr[i])
                count = 0
        return res




