class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path is None:
            return None
        # get the name in path
        names = []
        i = 0
        while i < len(path):
            # 跳过连续的 "/"
            while i < len(path) and path[i] == "/":
                i += 1

            s = []
            while i < len(path) and path[i] != "/":
                s.append(path[i])
                i += 1
            str = "".join(s)
            if str == "..":
                if len(names) > 0:
                    names.pop()
            elif (len(str) > 0 and str != "."):
                names.append(str)
        # get the result
        res = []
        if len(names) == 0:
            return "/"
        else:
            for name in names:
                res.append("/" + name)
            return "".join(res)

x = "/.."
s = Solution()
ans = s.simplifyPath(x)





