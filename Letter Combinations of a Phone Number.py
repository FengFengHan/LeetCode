class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        letters = [[] for _ in range(10)]
        count = 0
        for i in range(2,10):
            end = 4 if (i ==7 or i == 9) else 3
            for j in range(0,end):
                letters[i].append(chr(ord("a") + count))
                count += 1

        res = self.letterCombinationsHelp(digits,letters)
        res = ["".join(charList) for charList in res]
        return res

    def letterCombinationsHelp(self,digits,letters):
        if len(digits) == 0:
            return [[]]
        res = []
        num = int(digits[0])
        subRes = self.letterCombinationsHelp(digits[1:],letters)
        for i in range(len(letters[num])):
            tmp = [letters[num][i]]
            for j in range(len(subRes)):
                res.append(tmp + subRes[j])
        return res








