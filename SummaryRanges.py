__author__ = 'Administrator'
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        result = []
        if len(nums) == 0:
          return result

        start = nums[0]
        pre = nums[0]
        del nums[0]

        for num in nums:
            if (num - pre) != 1:
                end = pre
                if end == start:
                    result.append(str(start))
                else:
                   result.append(str(start) + "->" + str(end))
                start = num
            pre = num

        end = pre
        if end == start:
            result.append(str(start))
        else:
           result.append(str(start) + "->" + str(end))

        return result





