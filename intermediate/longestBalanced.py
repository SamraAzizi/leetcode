class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_len = 0
        
        for i in range(n):
            freq = {}
            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1
                
                # Check if balanced
                values = list(freq.values())
                if len(set(values)) == 1:
                    max_len = max(max_len, j - i + 1)
                
                # Early optimization
                if max_len >= n - i:
                    break
        
        return max_len