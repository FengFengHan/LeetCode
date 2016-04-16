class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # row and col
        for way in range(2):
            for line in range(9):
                occur = set()
                for i in range(9):
                    char_ = board[line][i] if way == 0 else board[i][line]
                    if char_ == ".":
                        continue
                    if not char_ in occur:
                        occur.add(char_)
                    else:
                        return False
        # 9 subset
        for i in range(0,9,3):
            for j in range(0,9,3):
                occur = set()
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        char_ = board[row][col]
                        if char_ == ".":
                            continue
                        if not char_ in occur:
                            occur.add(char_)
                        else:
                            return False
        return True