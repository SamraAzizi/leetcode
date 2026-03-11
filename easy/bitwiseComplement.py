class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        res = 0
        bit = 1

        while n > 0:
            res += (n % 2 ^ 1) * bit
            n //= 2
            bit *= 2

        return res