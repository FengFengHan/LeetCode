class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_ = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        nums = []
        for char in s:
            nums.append(dict_[char])
        res = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] < nums[i + 1]:
                res += nums[i + 1] - nums[i]
                i += 2
            else:
                res += nums[i]
                i += 1
        if i == len(nums) - 1:
            res += nums[i]
        return res
