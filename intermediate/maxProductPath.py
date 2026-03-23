class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        
        # Initialize dp arrays for max and min products
        max_prod = [[0] * n for _ in range(m)]
        min_prod = [[0] * n for _ in range(m)]
        
        max_prod[0][0] = min_prod[0][0] = grid[0][0]
        
        # Fill the first row and first column
        for i in range(1, m):
            max_prod[i][0] = min_prod[i][0] = max_prod[i-1][0] * grid[i][0]
        
        for j in range(1, n):
            max_prod[0][j] = min_prod[0][j] = max_prod[0][j-1] * grid[0][j]
        
        # Fill the rest of the dp arrays
        for i in range(1, m):
            for j in range(1, n):
                candidates = [
                    max_prod[i-1][j] * grid[i][j],
                    min_prod[i-1][j] * grid[i][j],
                    max_prod[i][j-1] * grid[i][j],
                    min_prod[i][j-1] * grid[i][j]
                ]
                max_prod[i][j] = max(candidates)
                min_prod[i][j] = min(candidates)
        
        result = max_prod[m-1][n-1]
        return result % mod if result >= 0 else -1