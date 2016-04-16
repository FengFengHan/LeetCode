class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        findCount = {}
        for char_ in t:
            if findCount.get(char_,None) == None:
                findCount[char_] = 0
            findCount[char_] += 1
        t_uniqueCount = len(findCount)
        minLen = len(s) + 1
        minPos = -1
        indexs = []
        for i in range(len(s)):
            if s[i] in findCount:
                findCount[s[i]] -= 1
                if findCount[s[i]] == 0:
                    t_uniqueCount -= 1
                indexs.append(i)
                if t_uniqueCount == 0:
                    while True:
                        if findCount[s[indexs[0]]] < 0:
                            findCount[s[indexs[0]]] += 1
                            del indexs[0]
                        else:
                            break
                    curLen = indexs[-1] - indexs[0] + 1
                    if curLen < minLen:
                        minLen = curLen
                        minPos = indexs[0]
        if minPos == -1:
            return ""
        return s[minPos:minPos+minLen]







