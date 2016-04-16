class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        ori = nums[:]
        nums.sort()
        low = 0
        high = len(nums) - 1
        while low < high:
            sum_ = nums[low] + nums[high]
            if sum_ == target:
                for i in range(len(ori)):
                    if ori[i] == nums[low] or ori[i] == nums[high]:
                        res.append(i+1)
                break
            elif sum_ > target:
                high -= 1
            else:
                low += 1
        return res

