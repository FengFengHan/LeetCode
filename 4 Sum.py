class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            # if nums[i] > target:   wrong because nums[i] can add a negative
            #     return res
            if i > 0 and nums[i] == nums[i- 1]:
                continue
            for j in range(i + 1,len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                sum_ = nums[i] + nums[j]
                l =  j + 1
                r = len(nums) -1
                while l < r:
                    total = sum_ + nums[l] + nums[r]
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                    if total >= target:
                        val = nums[r]
                        r -= 1
                        while r > l and nums[r] == val:
                            r -= 1
                    if total <= target:
                        val = nums[l]
                        l += 1
                        while l < r and nums[l] == val:
                            l += 1
        return res

x = [-3,-2,-1,0,0,1,2,3]
tar = 0
s = Solution()
ans =s.fourSum(x,tar)



