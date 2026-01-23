import heapq

class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        
        # 1. EARLY CHECK: If already sorted, no operations needed
        already_sorted = True
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                already_sorted = False
                break
        if already_sorted:
            return 0
        
        # 2. DATA STRUCTURES SETUP
        
        # Simulate doubly linked list using arrays:
        # prev[i] = index of previous element, or -1 if none
        # nxt[i] = index of next element, or -1 if none
        prev = list(range(-1, n-1))
        nxt = list(range(1, n+1))
        nxt[-1] = -1  # Last element has no next
        
        # Store values separately (we'll modify them)
        values = nums[:]
        
        # Track which elements are still active (not merged)
        valid = [True] * n
        
        # 3. INITIALIZE MIN-HEAP
        # Heap stores (sum, left_index) for all adjacent pairs
        heap = []
        for i in range(n-1):
            heapq.heappush(heap, (values[i] + values[i+1], i))
        
        # 4. TRACK DECREASING PAIRS COUNT
        # Instead of checking entire array each time,
        # maintain count of indices i where values[i] > values[i+1]
        decreasing_count = 0
        for i in range(n-1):
            if values[i] > values[i+1]:
                decreasing_count += 1
        
        ops = 0  # Operation counter
        
        # 5. MAIN LOOP: Continue while there are decreasing pairs
        while decreasing_count > 0:
            # Get minimum valid sum pair from heap
            while heap:
                s, left = heapq.heappop(heap)
                
                # Skip if left element was merged
                if not valid[left]:
                    continue
                    
                right = nxt[left]
                # Skip if right element doesn't exist or was merged
                if right == -1 or not valid[right]:
                    continue
                    
                # Skip if sum changed due to previous merges
                if values[left] + values[right] != s:
                    continue
                
                # FOUND VALID MINIMUM PAIR TO MERGE
                
                # 6. COUNT DECREASING PAIRS AROUND MERGE POINT (BEFORE)
                old_decreasing = 0
                
                # Check pair (prev[left], left)
                left_prev = prev[left]
                if left_prev != -1 and values[left_prev] > values[left]:
                    old_decreasing += 1
                
                # Check pair (left, right) - the pair we're merging
                if values[left] > values[right]:
                    old_decreasing += 1
                
                # Check pair (right, next[right])
                right_next = nxt[right]
                if right_next != -1 and values[right] > values[right_next]:
                    old_decreasing += 1
                
                # 7. PERFORM THE MERGE
                new_val = values[left] + values[right]
                values[left] = new_val
                valid[right] = False  # Mark right element as removed
                
                # Update linked list pointers
                nxt[left] = right_next
                if right_next != -1:
                    prev[right_next] = left
                
                # 8. COUNT DECREASING PAIRS AROUND MERGE POINT (AFTER)
                new_decreasing = 0
                
                # Check new pair (prev[left], left)
                if left_prev != -1 and values[left_prev] > new_val:
                    new_decreasing += 1
                
                # Check new pair (left, next[left])
                if right_next != -1 and new_val > values[right_next]:
                    new_decreasing += 1
                
                # 9. UPDATE DECREASING COUNT
                # Remove old decreasing pairs, add new ones
                decreasing_count = decreasing_count - old_decreasing + new_decreasing
                
                # 10. ADD NEW PAIRS TO HEAP
                if left_prev != -1:
                    heapq.heappush(heap, (values[left_prev] + new_val, left_prev))
                if right_next != -1:
                    heapq.heappush(heap, (new_val + values[right_next], left))
                
                ops += 1
                break  # Found and processed one merge
        
        return ops