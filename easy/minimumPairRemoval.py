class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = nums[:]
        ops = 0
        
        while True:
            # Check if non-decreasing
            non_dec = True
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    non_dec = False
                    break
            if non_dec:
                break
            
            # Find min sum adjacent pair
            min_sum = float('inf')
            min_idx = -1
            for i in range(len(arr) - 1):
                s = arr[i] + arr[i+1]
                if s < min_sum:
                    min_sum = s
                    min_idx = i
            
            # Merge
            arr[min_idx] = min_sum
            arr.pop(min_idx + 1)
            ops += 1
        
        return ops