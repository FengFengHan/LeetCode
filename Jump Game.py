class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        maxJumpPos = [0] * len(nums)
        for pos in xrange(len(nums)):
            maxJumpPos[pos] = pos + nums[pos]
        lastIndex = len(nums) -1
        pos = 0
        while True:
            nextPos = pos
            nextPosMax = maxJumpPos[nextPos]
            for j in range(pos+1,maxJumpPos[pos] + 1):
                if j >= lastIndex:
                    return True
                elif maxJumpPos[j] >= nextPosMax:
                    nextPos = j
                    nextPosMax = maxJumpPos[nextPos]
            if nextPos == pos:
                return False
            else:
                pos = nextPos



