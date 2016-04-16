class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        ind1 = m - 1
        ind2 = n - 1
        for i in range(m + n - 1, -1, -1):
            if ind2 < 0:
                break
            if ind1 >= 0 and nums1[ind1] > nums2[ind2]:
                nums1[i] = nums1[ind1]
                ind1 -= 1
            else:
                nums1[i] = nums2[ind2]
                ind2 -= 1



