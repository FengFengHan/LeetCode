class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.cand = sorted(candidates)
        self.tar = target
        self.last_used = -1
        self.path = []
        self.result = []
        self.dfs(0,0)
        return self.result

    #dfs(index, sum_): sum of items that has choosen is sum_, then choose element from  index to end
    def dfs(self, index, sum_):
        if sum_ == self.tar:
            self.result.append(self.path[:])
            return
        for i in range(index, len(self.cand)):
            if self.cand[i] == self.last_used:
                continue
            total = sum_ + self.cand[i]
            if total <= self.tar:
                self.path.append(self.cand[i])
                self.dfs(i + 1, total)
                self.path.pop()
                self.last_used = self.cand[i]
            else:
                break



