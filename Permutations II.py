class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = self.permuteUniqueHelper(nums)
        return res

    def permuteUniqueHelper(self,nums):
        if len(nums) == 1: return [[nums[0]]]
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            cur = [nums[i]]
            subRes = self.permuteUniqueHelper(nums[:i] + nums[i+1:])
            for j in range(len(subRes)):
                res.append(cur + subRes[j])
        return res
