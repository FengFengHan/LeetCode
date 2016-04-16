class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        indexs = {}
        for i in range(len(nums)):
            indexs.setdefault(nums[i], [])
            indexs[nums[i]].append(i)

        for lis in indexs.values():
            if len(lis) > 1:
                for j in range(1,len(lis)):
                    if (lis[j] - lis[j-1]) <= k:
                        return True
        return False

