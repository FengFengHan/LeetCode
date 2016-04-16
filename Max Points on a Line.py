# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)
        maxLen = 2
        for i in range(len(points)):
            point = points[i]
            k2Count = {}
            samePoint =0
            verticalPoint = 0
            for j in range(i+1,len(points)):
                if points[j].x == point.x and points[j].y == point.y:
                    samePoint += 1
                elif points[j].x == point.x:
                    verticalPoint += 1
                else:
                    k = ((float)(points[j].y - point.y))/ (points[j].x - point.x)
                    if k not in k2Count:
                        k2Count[k] = 1
                    else:
                        k2Count[k] += 1
            curMaxLen = samePoint + 1
            if len(k2Count) > 0:
                curMaxLen += max(verticalPoint, max(k2Count.values()))
            else:
                curMaxLen += verticalPoint
            if curMaxLen >maxLen:
                maxLen = curMaxLen
        return maxLen


