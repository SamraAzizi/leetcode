class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        for i in range(k // 2):
            # Swap rows: top row (x + i) with bottom row (x + k - 1 - i)
            top_row = x + i
            bottom_row = x + k - 1 - i
            
            # Swap elements in the submatrix columns [y, y + k - 1]
            for col in range(y, y + k):
                grid[top_row][col], grid[bottom_row][col] = grid[bottom_row][col], grid[top_row][col]
        
        return grid