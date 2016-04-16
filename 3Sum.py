class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        last_a = 0;
        last_b = 0;
        last_c = 0;
        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and a == last_a:
                continue
            if a > 0:
                break;
            for j in range(i + 1, len(nums)):
                b = nums[j]
                if j > i + 1 and b == last_b:
                    continue
                if a + b > 0:
                    break
                for k in range(j + 1, len(nums)):
                    c = nums[k]
                    if k > j + 1 and  c == last_c:
                        continue
                    if a + b + c > 0:
                        break
                    if (a + b + c) == 0:
                        result.append([a, b,c])
                        break
                    last_c = c
                last_b = b
            last_a = a
        return result


