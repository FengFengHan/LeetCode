class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        row = [1]
        row_old = row
        for i in range(1,rowIndex + 1):
            row = [1] * (i + 1)
            for j in range(1,i):
                row[j] = row_old[j-1] + row_old[j]
            row_old = row
        return row
