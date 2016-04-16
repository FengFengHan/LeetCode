class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        self.s1 = s1
        self.s2 = s2
        if len(s1) == 0:
            return True
        res = self.isScrambleHelp(0,len(s1),0,len(s2))
        return res

    def isScrambleHelp(self,b1,e1,b2,e2):
        lens = e1 - b1
        if lens == 1:
            if self.s1[b1] == self.s2[b2]:
                return True
            return False
        if sorted(self.s1[b1:e1]) != sorted(self.s2[b2:e2]):
            return False
        ne1 = b1 + lens // 2
        for ne1 in range(b1 + 1,e1):
            if self.isScrambleHelp(b1,ne1,b2,b2 + ne1 - b1) and self.isScrambleHelp(ne1,e1,e2 - e1 + ne1,e2):
                return True
            if self.isScrambleHelp(b1,ne1,e2-ne1+b1,e2) and self.isScrambleHelp(ne1,e1,b2,b2 + e1 -ne1):
                return True
        return False

s1 = "abb"
s2 = "bab"
s = Solution()
ans = s.isScramble(s1,s2)