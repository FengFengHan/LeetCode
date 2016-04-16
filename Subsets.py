class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.nums = nums
        self.n = len(nums)
        res = self.subsetsHelp(0)
        res.append([])
        return res

    def subsetsHelp(self,start):
        if start == self.n - 1:
            return [[self.nums[start]]]
        num = self.nums[start]
        sets = [[num]]
        subsets = self.subsetsHelp(start + 1)
        for subset in subsets:
            sets.append(subset)
            sets.append([num] + subset)
        return sets

x = [1,2]
s = Solution()
ans = s.subsets(x)