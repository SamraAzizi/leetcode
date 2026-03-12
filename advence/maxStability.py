class Solution(object):
    def maxStability(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Binary search on the answer (stability value)
        # Find max possible strength (original or doubled)
        max_strength = 0
        for edge in edges:
            max_strength = max(max_strength, edge[2])  # original
            if edge[3] == 0:  # can be upgraded
                max_strength = max(max_strength, edge[2] * 2)  # doubled
        
        left, right = 0, max_strength
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if self.canAchieve(n, edges, k, mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    def canAchieve(self, n, edges, k, target):
        """
        Check if we can build a spanning tree with stability >= target
        """
        # Union-Find data structure
        parent = list(range(n))
        
        def find(x):
            # Path compression
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[ry] = rx
            return True
        
        # Separate edges
        must_edges = []
        optional_edges = []
        
        for u, v, strength, must in edges:
            if must == 1:
                must_edges.append((u, v, strength))
            else:
                optional_edges.append((u, v, strength))
        
        # First, check if any must-include edge has strength < target
        # (they cannot be upgraded)
        for u, v, strength in must_edges:
            if strength < target:
                return False
        
        # Include all must-include edges first
        components = n
        # Reset parent for must-include check
        parent = list(range(n))
        
        for u, v, _ in must_edges:
            if not union(u, v):
                return False  # Cycle detected in must-include edges
            components -= 1
        
        # Now we need to connect the remaining components
        # Separate optional edges into those that meet target and those that need upgrade
        good_edges = []  # strength >= target (no upgrade needed)
        bad_edges = []   # strength < target (need upgrade)
        
        for u, v, strength in optional_edges:
            if strength >= target:
                good_edges.append((u, v))
            else:
                # Can this edge be upgraded to meet target?
                if strength * 2 >= target:
                    bad_edges.append((u, v))
                # Otherwise, it's useless for this target
        
        # Use good edges first (no upgrade cost)
        upgrades_used = 0
        
        for u, v in good_edges:
            if components == 1:
                break
            if union(u, v):
                components -= 1
        
        # Then try bad edges (require upgrades)
        for u, v in bad_edges:
            if components == 1:
                break
            if upgrades_used >= k:
                break
            if union(u, v):
                upgrades_used += 1
                components -= 1
        
        return components == 1