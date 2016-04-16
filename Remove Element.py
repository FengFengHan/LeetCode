class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        curLast = len(nums) - 1
        for i in range(len(nums)):
            if i > curLast:
                break
            if nums[i] == val:
                while curLast > i and nums[curLast] == val:
                    curLast -= 1
                if curLast == i:
                    curLast -= 1
                    break
                nums[i], nums[curLast] = nums[curLast], nums[i]
                curLast -= 1
        curLen = curLast + 1
        return curLen

x = [2,2,3]
s = Solution()
ans = s.removeElement(x,2)