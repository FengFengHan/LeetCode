class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        self.matrix = matrix
        res = self.spiralOrderHelp(0,0,len(matrix),len(matrix[0]))
        return res

    def spiralOrderHelp(self,startRow,startCol, endRow, endCol):
        if startRow >= endRow or startCol >= endCol:
            return []
        res = []
        top = self.matrix[startRow][startCol:endCol]
        right =[self.matrix[row][endCol-1] for row in range(startRow+ 1,endRow-1)]
        res = res + top + right
        if endRow - 1 !=  startRow:
            #bottom = self.matrix[endRow-1][endCol-1:-1:-1]  when endCol == 1 Ê±·¢Éú´íÎó
            if startCol != 0:
                bottom = self.matrix[endRow-1][endCol-1:startCol-1:-1]
            else:
                bottom = self.matrix[endRow-1][::-1]
            res += bottom
        if startCol != endCol - 1:
            left = [self.matrix[row][startCol] for row in range(endRow-2,startRow,-1)]
            res += left
        res += self.spiralOrderHelp(startRow + 1,startCol+ 1, endRow - 1 , endCol - 1)
        return res

x = [[3],[2]]
s = Solution()
ans = s.spiralOrder(x)

