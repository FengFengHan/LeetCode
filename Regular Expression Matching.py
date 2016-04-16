class Solution(object):
    cache = {}
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # p = self._compile(p)
        i = 0
        j = 0
        while i < len(s) and j < len(p):
            if j + 1 <len(p) and p[j+1] == "*":
                # if p[j] == s[i] and self.isMatch(s[i+1:],p[j:]):
                #
                #     return True
                # j += 2
                while True:
                    if (s[i:],p[j+2:]) not in self.cache:
                        self.cache[(s[i:],p[j+2:])] = self.isMatch(s[i:],p[j+2:])
                    if self.cache[(s[i:],p[j+2:])]:
                        return True
                    if i < len(s) and (s[i] == p[j] or p[j] == "."):
                        i += 1
                    else:
                        break
                if (s[i:],p[j+2:]) not in self.cache:
                    self.cache[(s[i:],p[j+2:])] = self.isMatch(s[i:],p[j+2:])
                return self.cache[(s[i:],p[j+2:])]
            elif (s[i] != p[j] and p[j] != "."):
                return False
            else:
                i += 1
                j += 1
        if i < len(s):
            return False
        while j < len(p):
            if p[j] != '*' and (j == len(p)- 1 or p[j+1] != '*'):
                return False
            j += 1
        return True


s= "aaaaaaaaaaaaab"
p = "a*a*a*a*a*a*a*a*a*a*c"
x =Solution()
ans = x.isMatch(s,p)