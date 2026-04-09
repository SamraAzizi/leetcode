class Solution(object):
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        
        import math
        B = int(math.sqrt(n)) + 1
        
        groups = {}
        large_queries = []
        
        for i, (l, r, k, v) in enumerate(queries):
            if k <= B:
                key = (k, l % k)
                if key not in groups:
                    groups[key] = []
                groups[key].append(i)
            else:
                large_queries.append(i)
        
        for (k, rem), qs in groups.items():
            m = (n - rem + k - 1) // k  
            diff = [1] * (m + 1)
            
            for qi in qs:
                l, r, _, v = queries[qi]
                start = (l - rem + k - 1) // k
                end = (r - rem) // k
                
                if start <= end:
                    diff[start] = diff[start] * v % MOD
                    inv_v = pow(v, MOD - 2, MOD)
                    diff[end + 1] = diff[end + 1] * inv_v % MOD
            
            cur = 1
            idx = rem
            for i in range(m):
                cur = cur * diff[i] % MOD
                nums[idx] = nums[idx] * cur % MOD
                idx += k
        
        for qi in large_queries:
            l, r, k, v = queries[qi]
            idx = l
            while idx <= r:
                nums[idx] = nums[idx] * v % MOD
                idx += k
        
        res = 0
        for x in nums:
            res ^= x
        
        return res