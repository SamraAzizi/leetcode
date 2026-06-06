class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_sum = 0
        right_sum = sum(nums)
        result = []

        for i in range(n):
            right_sum -= nums[i]
            result.append(abs(left_sum - right_sum))
            left_sum += nums[i]

        return result