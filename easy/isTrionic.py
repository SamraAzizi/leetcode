class Solution(object):
    def isTrionic(self, nums):
        """
        :type n: int
        :rtype: bool
        """
        n = len(nums)
        if n < 4:
            return False
        
        # Find p where prefix is increasing and next starts decreasing
        p = 0
        while p < n-1 and nums[p] < nums[p+1]:
            p += 1
        if p == 0 or p >= n-2:
            return False  # No increasing prefix of length >= 2 or no room for q
        
        # Now nums[p] is a peak, need decreasing then increasing
        # Find q where decreasing stops
        q = p
        while q < n-1 and nums[q] > nums[q+1]:
            q += 1
        if q == p:
            return False  # No decreasing part
        
        # Check if suffix from q is strictly increasing
        for i in range(q, n-1):
            if nums[i] >= nums[i+1]:
                return False
        return q < n-1  # q must be < n-1 for last part to have at least 2 elements