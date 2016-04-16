class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num_9 = 0
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] == 9:
                num_9 += 1
            else:
                break
        result = [0] * n
        if num_9 == n:
            result.append(0)
            result[0] = 1
        else:
           pos = n - 1 - num_9
           result[pos] = digits[pos] + 1
           result[0:pos] = digits[0:pos]
        return result
