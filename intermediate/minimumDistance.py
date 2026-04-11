class Solution:
    def minimumDistance(self, nums):
        last = {}
        second_last = {}
        ans = float('inf')
        
        for i, val in enumerate(nums):
            if val in second_last:
                ans = min(ans, 2 * (i - second_last[val]))
            
            if val in last:
                second_last[val] = last[val]
            
            last[val] = i
        
        return ans if ans != float('inf') else -1