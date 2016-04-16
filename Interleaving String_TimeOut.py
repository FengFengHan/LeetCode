class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        if len(s3) != (len(s1) + len(s2)):
            return False
        res = self.isInterleaveHelp(0,0,0)
        return res

    def isInterleaveHelp(self,start1,start2,start3):
        if start3 == len(self.s3):
            return True
        if start1 < len(self.s1) and self.s3[start3] == self.s1[start1]:
            if self.isInterleaveHelp(start1 + 1,start2,start3+1):
                return True
        if start2 < len(self.s2) and self.s3[start3] == self.s2[start2]:
            if self.isInterleaveHelp(start1,start2+1,start3+1):
                return True
        return False