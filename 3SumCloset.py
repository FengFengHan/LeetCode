class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        min_ = abs(res - target)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            r = i + 1
            l = len(nums) - 1
            while r < l:
                sum_ = nums[i] + nums[r] + nums[l]
                diff = sum_ - target
                if abs(diff) < min_:
                    min_ = abs(diff)
                    res = sum_
                if diff > 0:
                    l = l - 1
                elif diff < 0:
                    r = r + 1
                else:
                    return res
        return res
