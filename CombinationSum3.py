class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.n = n
        self.k = k
        path = []
        self.result = []
        self.dfs(1,0, path)
        return self.result

    def dfs(self, index, sum_, path):
        if sum_ == self.n and len(path) == self.k:
            self.result.append(path[:])
        if len(path) == self.k:
            return
        for i in range(index, 10):
            total  = sum_ + i
            if total <= self.n:
                path.append(i)
                self.dfs(i + 1, total, path)
                path.pop()
            else:
                break
