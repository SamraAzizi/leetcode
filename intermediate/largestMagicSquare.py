class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def is_magic(x, y, size):
            target = sum(grid[x][y:y+size])
            for i in range(size):
                if sum(grid[x+i][y:y+size]) != target:
                    return False
                if sum(grid[x+j][y+i] for j in range(size)) != target:
                    return False
            if sum(grid[x+i][y+i] for i in range(size)) != target:
                return False
            if sum(grid[x+i][y+size-1-i] for i in range(size)) != target:
                return False
            return True

        n, m = len(grid), len(grid[0])
        max_size = 1

        for size in range(2, min(n, m) + 1):
            for i in range(n - size + 1):
                for j in range(m - size + 1):
                    if is_magic(i, j, size):
                        max_size = size

        return max_size