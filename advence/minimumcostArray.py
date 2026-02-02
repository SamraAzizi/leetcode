class Solution(object):
    def minimumCost(self, nums, k, dist):
        """
        :type nums: List[int]
        :type k: int
        :type dist: int
        :rtype: int
        """
        n = len(nums)
        # We need to choose k-1 starting indices: i1, i2, ..., i_{k-1}
        # with i_{k-1} - i1 <= dist
        # Minimize nums[0] + nums[i1] + ... + nums[i_{k-1}]
        # Fixed: nums[0]
        # Need min sum of k-1 indices with constraint
        
        m = k - 2  # number of additional indices to pick after i1
        
        # For each i1, pick smallest m from (i1, i1+dist]
        # Then total = nums[0] + nums[i1] + sum_smallest_m
        
        # Initial window for i1 = 1: indices (1, 1+dist]
        window = SortedList()
        # Fill initial window
        for j in range(2, min(2 + dist, n)):
            window.add(nums[j])
        
        # Maintain smallest m in window
        # We'll keep track of sum of smallest m
        small = SortedList()
        large = SortedList(window)
        sum_small = 0
        
        # Initialize: take smallest m from large to small
        for _ in range(min(m, len(large))):
            val = large[0]
            large.pop(0)
            small.add(val)
            sum_small += val
        
        ans = float('inf')
        
        # Try each i1
        for i1 in range(1, n - (k - 1) + 1):
            # Current total if we choose i1
            if len(small) == m:  # we have enough elements
                total = nums[0] + nums[i1] + sum_small
                ans = min(ans, total)
            
            # Move window: remove nums[i1+1] if it's in range
            remove_idx = i1 + 1
            if remove_idx < n:
                val_to_remove = nums[remove_idx]
                # Remove from small or large
                if small and val_to_remove <= small[-1]:
                    # In small
                    idx = small.bisect_left(val_to_remove)
                    if idx < len(small) and small[idx] == val_to_remove:
                        small.pop(idx)
                        sum_small -= val_to_remove
                        # Move one from large to small if large not empty
                        if large:
                            val = large[0]
                            large.pop(0)
                            small.add(val)
                            sum_small += val
                else:
                    # In large
                    idx = large.bisect_left(val_to_remove)
                    if idx < len(large) and large[idx] == val_to_remove:
                        large.pop(idx)
            
            # Add new element at right end: nums[i1+dist+1]
            add_idx = i1 + dist + 1
            if add_idx < n:
                val_to_add = nums[add_idx]
                # Add to appropriate list
                if small and val_to_add < small[-1]:
                    # Move largest in small to large, add new to small
                    if len(small) == m:
                        move_val = small[-1]
                        small.pop()
                        sum_small -= move_val
                        large.add(move_val)
                    small.add(val_to_add)
                    sum_small += val_to_add
                else:
                    large.add(val_to_add)
            
            # Rebalance: ensure small has exactly m elements
            while len(small) > m and small:
                move_val = small[-1]
                small.pop()
                sum_small -= move_val
                large.add(move_val)
            while len(small) < m and large:
                move_val = large[0]
                large.pop(0)
                small.add(move_val)
                sum_small += move_val
        
        return ans