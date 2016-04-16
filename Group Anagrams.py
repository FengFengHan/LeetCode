class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return [[""]]
        anagrams = {}
        for str in strs:
            key_ = "".join(sorted(str))
            if anagrams.has_key(key_):
                anagrams[key_].append(str)
            else:
                anagrams[key_] = [str]
        res = []
        for value in anagrams.values():
            res.append(sorted(value))
            #res.append(value.sort()) does not work
        return res
x = ["han","hui"]
s = Solution()
ans = s.groupAnagrams(x)

