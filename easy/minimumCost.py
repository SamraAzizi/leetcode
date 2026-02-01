class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_cost = float('inf')
        for i in range(0, n-2):  # i can go up to n-3
            for j in range(i+1, n-1):  # j can go up to n-2
                cost = nums[0] + nums[i+1] + nums[j+1]
                min_cost = min(min_cost, cost)
        return min_cost