class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #ͳ�����ֳ��ֵĴ���
        num2count = {}
        for num in nums:
            if num2count.get(num,None) == None:
                num2count[num] = 0
            num2count[num] += 1
        #ʹ�����б�Ϊ�����ظ����֣�������
        nums = list(set(nums))
        nums.sort()
        n = len(nums)

        res = []
        for i in range(2 ** n):
            curRes = [[]]
            for j in range(n):
                if(i >> j & 1):
                    selNum = nums[j]
                    preRes = curRes
                    curRes = []
                    for k in range(len(preRes)):
                        for m in range(1,num2count[selNum] + 1):
                            curRes.append(preRes[k] + ([selNum] * m) )
            res += curRes
        return res