class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0 or len(s) == 0:
            return []
        length = len(words[0])
        n = len(words)
        if length * n > len(s):
            return []

        res = []
        wordsCount = {}
        for word in words:
            if word not in wordsCount:
                wordsCount[word] = 0
            wordsCount[word] += 1
        for round_ in range(length):
            cnt = 0 #number of word which belong to words in s
            start = -1
            occurCount = {}
            for word in wordsCount:
                occurCount[word] = 0
            for i in range(round_,len(s),length):
                word = s[i:i+length]
                if word in wordsCount:
                    if start == -1:
                        start = i
                    if occurCount[word] < wordsCount[word]:
                        occurCount[word] += 1
                        cnt += 1
                        if cnt == n:
                            res.append(start)
                    elif occurCount[word] == wordsCount[word]:
                        for j in range(start,i,length):
                            wordtmp = s[j:j+length]
                            if wordtmp != word:
                                occurCount[wordtmp] -= 1
                                cnt -= 1
                            else:
                                start = j + length
                                if cnt == n:
                                    res.append(start)
                                break
                else:
                    if start != -1:
                        for j in range(start,i,length):
                            wordtmp = s[j:j+length]
                            occurCount[wordtmp] = 0
                            cnt -= 1
                    start = -1
        return res

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

S = Solution()
ans = S.findSubstring(s,words)
print("debug")



