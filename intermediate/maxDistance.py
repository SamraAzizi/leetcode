class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i, j = 0, 0
        max_distance = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                max_distance = max(max_distance, j - i)
                j += 1
            else:
                i += 1

        return max_distance