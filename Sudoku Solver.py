class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.char2Ind = {}
        for i in range(1,10):
            self.char2Ind[str(i)] = 1 << (i-1)
        r,c,s = [0] * 9, [0]*9, [0]*9 # row,col,sub
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = self.char2Ind[board[i][j]]
                r[i] |= num
                c[j] |= num
                s[i//3 * 3 + j//3] |= num
        self.solveSudoKuHelp(board,r,c,s)

    def solveSudoKuHelp(self,board,r,c,s):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for char_ in "123456789":
                        num = self.char2Ind[char_]
                        if (num & (~(r[i] | c[j] | s[i//3*3 + j//3]))) != 0:
                            board[i][j] = char_
                            r[i] |= num
                            c[j] |= num
                            s[i//3*3 + j//3] |= num
                            if self.solveSudoKuHelp(board,r,c,s):
                                return True
                            board[i][j] = "."
                            r[i] &= (~num)
                            c[j] &= (~num)
                            s[i//3*3 + j//3] &= (~num)
                    return False
        return True

x = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
s = Solution()
ans = s.solveSudoKu(x)