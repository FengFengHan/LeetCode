# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        i = 0
        while i < len(intervals):
            # non-overlapping and merge with newInterval has finished
            if intervals[i].start > newInterval.end:
                res.append(newInterval)
                res.extend(intervals[i:])
                break
            # non-overlapping
            elif intervals[i].end < newInterval.start:
                res.append(intervals[i])
                i += 1
            # merge
            else:
                newInterval.start = min(newInterval.start,intervals[i].start)
                newInterval.end = max(newInterval.end,intervals[i].end)
                i += 1
                while i < len(intervals) and newInterval.end >= intervals[i].start:
                    newInterval.end = max(newInterval.end,intervals[i].end)
                    i += 1
        if i == len(intervals):
            res.append(newInterval)
        return res
