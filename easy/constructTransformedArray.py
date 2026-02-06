class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            if nums[i] == 0:
                result[i] = 0
            elif nums[i] > 0:
                # Move right nums[i] steps
                new_index = (i + nums[i]) % n
                result[i] = nums[new_index]
            else:  # nums[i] < 0
                # Move left abs(nums[i]) steps
                new_index = (i - abs(nums[i])) % n
                result[i] = nums[new_index]
        
        return result