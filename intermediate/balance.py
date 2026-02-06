class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        
        nums.sort()
        max_len = 1  # at least one element always valid
        
        right = 0
        for left in range(n):
            # Expand right as far as possible
            while right < n and nums[right] <= k * nums[left]:
                right += 1
            # Now nums[right] > k*nums[left] or right==n
            # Valid window is [left, right-1]
            window_len = right - left
            max_len = max(max_len, window_len)
        
        return n - max_len