class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        # record row and col that are zeroed
        zeroRow = {}
        for row in range(m):
            zeroRow[row] = False
        zeroCol = {}
        for col in range(n):
            zeroCol[col] = False
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroRow[row] = True
                    zeroCol[col] = True
        # set zeros
        for row in range(m):
            for col in range(n):
                if zeroRow[row] or zeroCol[col]:
                    matrix[row][col] = 0
