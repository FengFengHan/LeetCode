class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                tmp = nums[nums[i] -1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

# x = [-10,-3,-100,-1000,-239,1]
x = [3,4,-1,1]
s = Solution()
ans = s.firstMissingPositive(x)