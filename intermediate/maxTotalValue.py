class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi = max(nums)
        mini = min(nums)
        return k * (maxi - mini)