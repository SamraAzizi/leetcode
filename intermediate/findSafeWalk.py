class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        n = len(grid)
        m = len(grid[0])
        start_health = health - grid[0][0]
        if start_health <= 0:
            return False
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        best = [[-1] * m for _ in range(n)]
        best[0][0] = start_health
        q = deque()
        q.append((0, 0, start_health))
        while q:
            r, c, curr_health = q.popleft()
            if r == n - 1 and c == m - 1:
                return True
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr >= n or nc >= m:
                    continue
                new_health = curr_health - grid[nr][nc]
                if new_health <= 0:
                    continue
                if best[nr][nc] >= new_health:
                    continue
                best[nr][nc] = new_health
                q.append((nr, nc, new_health))
        return False
