# coding: utf-8
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        marked = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                marked[(i,j)] = False
        path = []
        di = [[0,1],[1,0],[0,-1],[-1,0]] #方向
        pos = self.serachChar(board,word[0],0,0)
        if not self.validPos(pos,board): return False
        path.append([pos,0]) #位置和下一个点的方向
        marked[pos] = True #pos是否已经在path中
        while len(path) < len(word):
            cur = path[-1]
            i = cur[1]
            while i < 4:
                nextPos = (cur[0][0] + di[i][0], cur[0][1] + di[i][1])
                if self.validPos(nextPos,board) and not marked[nextPos] and board[nextPos[0]][nextPos[1]] == word[len(path)]:
                    path.append([nextPos,0])
                    marked[nextPos] = True
                    break
                i += 1
            cur[1] = i + 1
            if cur[1] > 4:
                deled = path.pop()
                marked[deled[0]] = False
                if len(path) == 0:
                    pos = self.serachChar(board,word[0],deled[0][0],deled[0][1] + 1)
                    if not self.validPos(pos,board):return False
                    path.append([pos,0])
                    marked[pos] = True
        return True

    def validPos(self,pos,board):
        if pos[0] < 0 or pos[0] >= len(board) or pos[1] < 0 or pos[1] >= len(board[0]):
            return False
        return True

    def serachChar(self,borad,char_,x,y):
        for j in range(y,len(borad[0])):
            if borad[x][j] == char_:
                return (x,j)
        for i in range(x+1,len(borad)):
            for j in range(len(borad[0])):
                if borad[i][j] == char_:
                    return (i,j)
        return (-1,-1)

