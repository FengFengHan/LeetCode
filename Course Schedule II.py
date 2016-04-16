class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        preCount = [0] * numCourses
        afterCourses = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            preCount[prerequisite[0]] += 1
            afterCourses[prerequisite[1]].append(prerequisite[0])
        curCourses = []
        for i in range(numCourses):
            if preCount[i] == 0:
                curCourses.append(i)
        while len(curCourses) > 0:
            curCourse = curCourses.pop()
            res.append(curCourse)
            for course in afterCourses[curCourse]:
                preCount[course] -= 1
                if preCount[course] == 0:
                    curCourses.append(course)
        if len(res) == numCourses:
            return  res
        return []

