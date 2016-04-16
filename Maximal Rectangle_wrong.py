class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        startRow, endRow = len(matrix), -1
        startCol, endCol = len(matrix[0]), - 1
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    if row < startRow: startRow = row
                    if row > endRow: endRow = row
                    if col < startCol:startCol = col
                    if col > endCol: endCol = col
        if endRow == -1:
            return 0
        area = (endRow -startRow + 1) * (endCol - startCol + 1)
        return area