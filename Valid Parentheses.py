class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # to facilate express and compute,change the char to num
        nums = []
        charToNum = {"(":1, ")":2, "[":3, "]":4, "{":5, "}":6}
        for i in range(len(s)):
            nums.append(charToNum[s[i]])
        for num in nums:
            if num % 2 == 1:
                stack.append(num)
            else:
                if len(stack) > 0 and stack.pop() == num - 1:
                    pass
                else:
                    return False
        if len(stack) == 0:
            return True
        return False



