class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        n = len(s)
        for i in range(3):
            ip = [0] * 4
            if i >= n: return res
            s1 = s[0:i+1]
            if self.isInIp(s1):
                ip[0] = s1
            else:
                continue
            for j in range(i+1,i+4):
                if j >= n: break
                s1 = s[i+1:j+1]
                if self.isInIp(s1):
                    ip[1] = s1
                else:
                    continue
                for k in range(j+1,j+4):
                    if k >= n:  break
                    s1 = s[j+1:k+1]
                    if self.isInIp(s1):
                        ip[2] = s1
                    else:
                        continue
                    s1 = s[k+1:]
                    if len(s1) > 0 and len(s1) <= 3 and self.isInIp(s1):
                        ip[3] = s1
                        res.append(".".join(ip))
        return res

    def isInIp(self,s):
        if (len(s) > 1 and s[0] == "0") or(len(s) == 3 and int(s) > 255) :
            return False
        return True
x = "101023"
s = Solution()
ans= s.restoreIpAddresses(x)






