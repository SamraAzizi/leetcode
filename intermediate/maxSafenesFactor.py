class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]

        q = deque()
        dist = [[0] * n for _ in range(n)]
        vis = [[False] * n for _ in range(n)]

        # Step 1: Push all thief cells
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    vis[r][c] = True
                    q.append((r, c))

        # Multi-source BFS
        while q:
            r, c = q.popleft()

            for d in range(4):
                nr = r + dx[d]
                nc = c + dy[d]

                if nr < 0 or nc < 0 or nr >= n or nc >= n:
                    continue
                if vis[nr][nc]:
                    continue

                dist[nr][nc] = dist[r][c] + 1
                vis[nr][nc] = True
                q.append((nr, nc))

        # Step 2: Max heap for best safeness path
        store = []
        vis2 = [[False] * n for _ in range(n)]

        heapq.heappush(store, (-dist[0][0], 0, 0))

        while store:
            safeE, r, c = heapq.heappop(store)
            safeE = -safeE

            if vis2[r][c]:
                continue
            vis2[r][c] = True

            if r == n - 1 and c == n - 1:
                return safeE

            for d in range(4):
                nr = r + dx[d]
                nc = c + dy[d]

                if nr < 0 or nc < 0 or nr >= n or nc >= n:
                    continue
                if vis2[nr][nc]:
                    continue

                newSafe = min(safeE, dist[nr][nc])
                heapq.heappush(store, (-newSafe, nr, nc))

        return 0