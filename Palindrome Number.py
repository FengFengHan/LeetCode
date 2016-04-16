class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        digits = []
        while True:
            digits.append(x%10)
            x /= 10
            if x == 0:
                break
        for i in range(len(digits)//2):
            if digits[i] != digits[len(digits)-1-i]:
                return False
        return True
