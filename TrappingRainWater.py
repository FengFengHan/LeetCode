class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #max value of left and right
        maxl, maxr = height[:], height[:]
        max_ = 0
        for i in range(len(height)):
            if height[i] > max_:
                max_ = height[i]
            else:
                maxl[i] = max_
        max_ = 0
        for i in range(len(height) -1, -1, -1):
            if height[i] > max_:
                max_ = height[i]
            else:
                maxr[i] = max_
        #
        sumv = 0
        for i in range(len(height)):
            v = ( min(maxl[i], maxr[i]) - height[i])
            sumv += v if v > 0 else 0
        return sumv