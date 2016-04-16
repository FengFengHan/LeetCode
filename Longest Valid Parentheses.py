class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        #longset[i]: longestValidParentheses at position i when s[i] == ")"
        longest = [0] * len(s)
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
               stack.append(i)
            else:
                if len(stack) > 0:
                    left = stack.pop()
                    longest[i] = longest[i-1] + 2
                    if left > 0:
                        longest[i] += longest[left -1]
        return max(longest)

