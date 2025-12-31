class Solution(object):
    def latestDayToCross(self, row, col, cells):
        def canCross(day):
            grid = [[0] * col for _ in range(row)]
            for r, c in cells[:day]:
                grid[r - 1][c - 1] = 1

            visited = [[False] * col for _ in range(row)]

            def dfs(r, c):
                if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 1 or visited[r][c]:
                    return False
                if r == row - 1:
                    return True
                visited[r][c] = True
                return (dfs(r + 1, c) or dfs(r - 1, c) or
                        dfs(r, c + 1) or dfs(r, c - 1))

            for c in range(col):
                if grid[0][c] == 0 and dfs(0, c):
                    return True
            return False

        left, right = 0, len(cells)
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if canCross(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result