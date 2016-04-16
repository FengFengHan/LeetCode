class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        result = [[]] * numRows
        result[0].append(1)
        for i in range(1,numRows):
            result[i] = [1] * (i + 1)
            for j in range(1,i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result

