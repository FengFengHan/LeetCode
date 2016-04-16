class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        sz = 0
        while i < len(nums):
            value = nums[i]
            nums[sz] = value
            count = 1
            i += 1
            sz += 1
            while i < len(nums) and nums[i] == value:
                count += 1
                i += 1
            if count >= 2:
                nums[sz] = value
                sz += 1
        return sz


