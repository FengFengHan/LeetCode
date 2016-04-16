class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = self.permuteHelp(nums)
        return res
    def permuteHelp(self,nums):
        if len(nums) == 1:
            return [[nums[0]]]
        res = []
        for i in range(len(nums)):
            subRes = self.permuteHelp(nums[:i] + nums[i+1:])
            for j in range(len(subRes)):
                res.append([nums[i]] + subRes[j])
        return res