class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        graph = [[] for _ in range(n)]

        high = -1
        for u, v, w in edges:
            graph[u].append((v, w))
            high = max(high, w)

        low, ans = 0, -1

        while low <= high:
            mid = (low + high) // 2
            if self.check(graph, online, mid, k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

    def check(self, graph, online, mid, k):
        n = len(graph)
        cost = [float('inf')] * n
        cost[0] = 0

        heap = [(0, 0)]

        while heap:
            curr_cost, node = heapq.heappop(heap)

            if curr_cost > cost[node]:
                continue
            if node != 0 and node != n - 1 and not online[node]:
                continue

            for adj, wt in graph[node]:
                if wt < mid:
                    continue
                if adj != 0 and adj != n - 1 and not online[adj]:
                    continue

                new_cost = curr_cost + wt
                if new_cost > k:
                    continue

                if new_cost < cost[adj]:
                    cost[adj] = new_cost
                    heapq.heappush(heap, (new_cost, adj))

        return cost[-1] <= k