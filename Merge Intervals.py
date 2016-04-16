# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        if len(intervals) == 0:
            return res
        intervals = sorted(intervals,cmp = self.intervals_cmp)
        interval = intervals[0]
        for i in range(1,len(intervals)):
            tmp = intervals[i]
            if tmp.start <= interval.end:
                if tmp.end > interval.end:
                    interval.end = tmp.end
            else:
                res.append(interval)
                interval = tmp
        res.append(interval)
        return res

    def intervals_cmp(self,x,y):
        if x.start < y.start:
            return -1
        elif x.start == y.start:
            if x.end < y.end:
                return -1
            elif x.end == y.end:
                return 0
        return 1

        