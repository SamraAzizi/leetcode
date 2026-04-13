class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if start - i >= 0 and nums[start - i] == target:
                return i
            if start + i < n and nums[start + i] == target:
                return i