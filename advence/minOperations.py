class Solution(object):
    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        z = s.count('0')
        o = n - z
        
        if z == 0:
            return 0
        
        if k % 2 == 0 and z % 2 == 1:
            return -1
        
        if k == n:
            return 1 if z == n else -1
        
        min_m = (z + k - 1) // k
        
        m = min_m
        while m <= 2 * n + 10:
            if (k * m) % 2 != z % 2:
                m += 1
                continue
            
            if m % 2 == 1:
                if o <= (n - k) * m:
                    return m
            else:
                if z <= (n - k) * m:
                    return m
            
            m += 1
        
        return -1