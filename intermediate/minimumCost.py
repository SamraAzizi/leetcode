class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        
        INF = 10**18
        n = len(source)
        m = len(original)
        
        # Create adjacency matrix
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
            
        for o, c, co in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], co)
        
        # Floyd-Warshall
        for k in range(26):
            for i in range(26):
                if dist[i][k] == INF:
                    continue
                for j in range(26):
                    if dist[k][j] == INF:
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Calculate answer
        ans = 0
        for i in range(n):
            if source[i] == target[i]:
                continue
            u = ord(source[i]) - ord('a')
            v = ord(target[i]) - ord('a')
            if dist[u][v] == INF:
                return -1
            ans += dist[u][v]
            
        return ans