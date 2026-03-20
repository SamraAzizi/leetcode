class Solution(object):
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        result = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                # Extract all values in k×k window
                values = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        values.append(grid[x][y])
                
                # Sort and find min difference
                values.sort()
                min_diff = float('inf')
                for idx in range(1, len(values)):
                    if values[idx] != values[idx-1]:
                        min_diff = min(min_diff, values[idx] - values[idx-1])
                
                result[i][j] = min_diff if min_diff != float('inf') else 0
        
        return result