class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_nums = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))
        
        max_value = F
        
        for k in range(1, n):
            F = F + sum_nums - n * nums[n - k]
            max_value = max(max_value, F)
        
        return max_value