class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #从后向前寻找与开始形成回文的位置
        i = len(s) - 1
        while i > 0:
            nextPos = i - 1
            if s[i] == s[0]:
                low = 1
                high = i - 1
                while low <= high:
                    if s[high] != s[low]:
                        break
                    if s[high] == s[0] and nextPos == i -1:
                        nextPos = high
                    low += 1
                    high -= 1
                if low > high:
                    break
            i = nextPos
        front = ""
        front = front + s[len(s)-1:i:-1]
        s = front + s
        return s

