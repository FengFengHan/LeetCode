class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for i in range(n)]
        x,y = 0,0
        dx, dy ,dn = [0,1,0,-1],[1,0,-1,0],0
        visited = [False for i in range(n * n)]
        num = 1
        while num <= n ** 2:
            res[x][y] = num
            visited[x*n + y] = True
            x,y = x + dx[dn],y + dy[dn]
            if x >= n or x < 0 or y >= n or y < 0 or visited[x * n + y]:
                x,y = x -dx[dn],y-dy[dn]
                dn = (dn + 1) % 4
                x,y = x + dx[dn], y +  dy[dn]
            num += 1
        return res





