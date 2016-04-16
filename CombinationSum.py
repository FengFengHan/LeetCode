import time
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.cand = sorted(candidates)
        self.tar = target
        self.path = []
        self.result = []
        self.dfs(0,0)
        return self.result

    def dfs(self, index, sum_):
        if sum_ == self.tar:
            self.result.append(self.path[:])
            return
        for i in range(index, len(self.cand)):
            total = sum_ + self.cand[i]
            if total <= self.tar:
                self.path.append(self.cand[i])
                self.dfs(i, total)
                self.path.pop()
            else:
                break;


start = time.clock()
s = Solution()
y = [92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73]
tar = 310
s.combinationSum(y, tar)
elapse = (time.clock() - start)
print("time:", elapse)






