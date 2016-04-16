class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = [ord(c) - ord("0") for c in s]
        pre2,pre1,cur = 1,1,0
        if len(nums) > 0 and nums[0] > 0:
            cur = 1
        pre2,pre1 = pre1,cur
        for i in range(1,len(nums)):
            cur = 0
            tmp = nums[i-1] * 10 + nums[i]
            if nums[i] > 0:
                cur += pre1
            if tmp <= 26 and tmp >= 10:
                cur += pre2
            if cur == 0:
                break
            pre2,pre1 = pre1,cur
        return cur