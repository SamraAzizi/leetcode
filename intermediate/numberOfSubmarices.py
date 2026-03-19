class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        # Prefix count arrays: [x_count, y_count] for each cell
        prefix = [[[0, 0] for _ in range(n)] for _ in range(m)]
        
        # Build prefix counts
        for i in range(m):
            for j in range(n):
                # Get current cell's contribution
                x_contrib = 1 if grid[i][j] == 'X' else 0
                y_contrib = 1 if grid[i][j] == 'Y' else 0
                
                if i == 0 and j == 0:
                    # Top-left cell
                    prefix[i][j] = [x_contrib, y_contrib]
                elif i == 0:
                    # First row: add from left
                    prefix[i][j] = [
                        prefix[i][j-1][0] + x_contrib,
                        prefix[i][j-1][1] + y_contrib
                    ]
                elif j == 0:
                    # First column: add from above
                    prefix[i][j] = [
                        prefix[i-1][j][0] + x_contrib,
                        prefix[i-1][j][1] + y_contrib
                    ]
                else:
                    # General case: add from left + above - top-left (to avoid double count)
                    prefix[i][j] = [
                        prefix[i-1][j][0] + prefix[i][j-1][0] - prefix[i-1][j-1][0] + x_contrib,
                        prefix[i-1][j][1] + prefix[i][j-1][1] - prefix[i-1][j-1][1] + y_contrib
                    ]
        
        # Count valid submatrices
        count = 0
        for i in range(m):
            for j in range(n):
                x_count, y_count = prefix[i][j]
                if x_count == y_count and x_count > 0:
                    count += 1
        
        return count