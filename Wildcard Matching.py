class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        p_any = -1
        s_any_next = -1
        more_any_next = set()
        while i < len(s) and j <len(p):
            if p[j] == "*":
                p_any = j
                s_any_next = -1
                more_any_next = set()
                if j == len(p) - 1:
                    return True
                else:
                    if p[j+1] != "?":
                        while i < len(s) and s[i] != p[j+1]:
                            i += 1
                    s_any_next = i
                    i += 1
                    j += 2
            elif p[j] == "?" or s[i] == p[j]:
                if s[i] == s[s_any_next]:
                    more_any_next = more_any_next | {i}
                i += 1
                j += 1
            else:
                if p_any == -1:
                    return False
                else:
                    if len(more_any_next) == 0:
                        j = p_any
                    else:
                        j = p_any + 1
                        i = more_any_next.pop() + 1

        if i >= len(s) and (j >= len(p) or (j == len(p) - 1 and p[j] == "*")):
            return True
        else:
            return False

x1 = "abefcdgiescdfimde"
x2 = "ab*cd?i*de"
s =Solution()
ans = s.isMatch(x1,x2)
