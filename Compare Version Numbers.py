class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        versionNums1 = version1.split(".")
        versionNums2 = version2.split(".")
        i = 0
        while i < len(versionNums1) and i < len(versionNums2):
            if int(versionNums1[i]) > int(versionNums2[i]):
                return 1
            elif int(versionNums1[i]) < int(versionNums2[i]):
                return -1
            i += 1
        if i < len(versionNums1):
            for j in range(i,len(versionNums1)):
                if int(versionNums1[j]) != 0:
                    return 1
        elif i < len(versionNums2):
            for j in range(i,len(versionNums2)):
                if int(versionNums2[j]) != 0:
                    return -1
        return 0