class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        result = 0
        
        for i in range(1, n + 1):
            length = i.bit_length()
            result = ((result << length) | i) % mod
        
        return result