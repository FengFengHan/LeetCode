class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #start: 0 pointer£¬ p: traverse pointer, end: 2 pointer
        start, p, end = 0, 0, len(nums)-1
        while(p <= end):
            if nums[p] == 0:
                if p > start:
                    nums[start], nums[p] = nums[p], nums[start]
                p += 1
                start += 1
            elif nums[p] == 2:
                while end > p and nums[end] == 2:
                    end -= 1
                if p < end:
                    nums[p], nums[end] = nums[end], nums[p]
                end -= 1
            else:
                p += 1