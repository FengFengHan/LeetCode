class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alpnums = []
        for char in s:
            if char.isalnum():
                alpnums.append(char)
        alpnums = "".join(alpnums).lower()
        if len(alpnums) < 2:
            return True
        else:
            mid = (len(alpnums) + 1)//2
            if alpnums[0:mid] == alpnums[len(alpnums)-1:len(alpnums) - 1 - mid:-1]:
                return True
            else:
                return False

x = "a ba"
s = Solution()
ans = s.isPalindrome(x)
