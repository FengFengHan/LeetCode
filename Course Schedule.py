class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        afterCourse = [[] for i in range(numCourses)]
        preCount = [0] * numCourses
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            preCount[course] +=  1
            afterCourse[prerequisites[i][1]].append(course)
        curCourses = []
        for i in range(numCourses):
            if preCount[i] == 0:
                curCourses.append(i)
        doneCourse = 0
        while len(curCourses) > 0:
            curCourse = curCourses.pop()
            doneCourse += 1
            for course in afterCourse[curCourse]:
                preCount[course] -= 1
                if preCount[course] == 0:
                    curCourses.append(course)
        if doneCourse == numCourses:
            return True
        return False

num = 4
pre = [[0,1],[3,1],[1,3],[3,2]]
s = Solution()
ans = s.canFinish(num, pre)
