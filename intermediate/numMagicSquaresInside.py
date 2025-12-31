class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isMagic(x, y):
            nums = set()
            for i in range(3):
                for j in range(3):
                    val = grid[x + i][y + j]
                    if val < 1 or val > 9 or val in nums:
                        return False
                    nums.add(val)

            s = sum(grid[x][y:y + 3])
            for i in range(3):
                if sum(grid[x + i][y:y + 3]) != s:
                    return False
                if sum(grid[x + j][y + i] for j in range(3)) != s:
                    return False

            if sum(grid[x + i][y + i] for i in range(3)) != s:
                return False
            if sum(grid[x + i][y + 2 - i] for i in range(3)) != s:
                return False

            return True

        count = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    count += 1

        return count