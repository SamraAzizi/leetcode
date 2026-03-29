class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        total_sum = sum(sum(row) for row in grid)
        
        # If total sum is odd, we cannot partition it into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        rows, cols = len(grid), len(grid[0])
        
        # Create a set to store possible sums
        possible_sums = {0}
        
        for r in range(rows):
            new_sums = set()
            for c in range(cols):
                for s in possible_sums:
                    new_sums.add(s + grid[r][c])
            possible_sums.update(new_sums)
        
        return target in possible_sums