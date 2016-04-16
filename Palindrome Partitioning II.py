class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.palindromes = self.getPalindrome(s)
        minCutHere = [0] * len(s)
        for i in range(1,len(s)):
            minCutHere[i] = minCutHere[i-1] + 1
            for j in range(0,i):
                if self.isPalindrome(j,i):
                    if j == 0:
                        minCutHere[i] = 0
                    else:
                        minCutHere[i] = min(minCutHere[j-1] + 1,minCutHere[i])
        return minCutHere[-1]

    def getPalindrome(self,s):
        s1 = "#" + "#".join(s) + "#"
        id,mx = 0,0
        p = [1] * len(s1)
        for i in range(len(s1)):
            if mx > i:
                p[i] = min(p[2*id - i],mx-i)
            while i - p[i] >= 0 and i + p[i] < len(s1) and s1[i - p[i]] == s1[i + p[i]]:
                p[i] += 1
            if p[i] > mx:
                mx = i
                id = i
        return p
    def isPalindrome(self,left,right):
        if self.palindromes[left+right+1] > (right - left):
            return True
        return  False

