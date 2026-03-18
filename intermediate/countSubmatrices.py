class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        count = 0
        
        for top in range(m):
            sums = [0] * n
            for bottom in range(top, m):
                for col in range(n):
                    sums[col] += grid[bottom][col]
                
                # Count subarrays with sum <= k
                count += self.countSubarrays(sums, k)
        
        return count