class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        if n == 1:
            return 
        
        # There are two patterns for each row:
        # Pattern A: 3 ways (e.g., RGB, RBG, GRB)
        # Pattern B: 6 ways (e.g., RGR, RBR, GRG, GBG, BRB, BGB)
        
        # Let a be the number of ways to color the current row with Pattern A
        # Let b be the number of ways to color the current row with Pattern B
        
        a, b = 6, 6
        
        for _ in range(2, n + 1):
            new_a = (2 * a + 2 * b) % MOD
            new_b = (2 * a + 3 * b) % MOD
            a, b = new_a, new_b
        
        return (a + b) % MOD