import heapq
from typing import List
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency lists
        graph = defaultdict(list)  # outgoing edges
        incoming = defaultdict(list)  # incoming edges
        
        for u, v, w in edges:
            graph[u].append((v, w))
            incoming[v].append((u, w))  # edge from u to v
        
        # dist[node][switch_used_at_node]
        # 0 = not used, 1 = used
        dist = [[float('inf')] * 2 for _ in range(n)]
        dist[0][0] = 0
        
        pq = [(0, 0, 0)]  # (cost, node, switch_used)
        
        while pq:
            cost, u, used = heapq.heappop(pq)
            
            if cost > dist[u][used]:
                continue
            
            # 1. Normal moves: follow existing outgoing edges
            for v, w in graph[u]:
                new_cost = cost + w
                # Arrive at v, switch at v not used yet
                if new_cost < dist[v][0]:
                    dist[v][0] = new_cost
                    heapq.heappush(pq, (new_cost, v, 0))
            
            # 2. Use switch (if not used yet)
            if used == 0:
                # For each incoming edge to u, we can reverse it
                for v, w in incoming[u]:
                    # Reverse v→u to u→v with cost 2*w
                    new_cost = cost + 2 * w
                    # After reversing, we travel to v immediately
                    # We arrive at v with switch at v not used
                    if new_cost < dist[v][0]:
                        dist[v][0] = new_cost
                        heapq.heappush(pq, (new_cost, v, 0))
        
        # We can finish at n-1 with switch used or not
        result = min(dist[n-1][0], dist[n-1][1])
        return -1 if result == float('inf') else result