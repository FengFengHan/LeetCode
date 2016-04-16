class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        maxJumpPos = [0] * len(nums)
        for pos in xrange(len(nums)):
            maxJumpPos[pos] = pos + nums[pos]
        lastIndex = len(nums) -1
        pos = 0
        step = 0
        while True:
            nextPos = pos
            nextPosMax = maxJumpPos[nextPos]
            for j in range(pos+1,maxJumpPos[pos] + 1):
                if j >= lastIndex:
                    step += 1
                    return step
                elif maxJumpPos[j] >= nextPosMax:
                    nextPos = j
                    nextPosMax = maxJumpPos[nextPos]
            step += 1
            pos = nextPos




