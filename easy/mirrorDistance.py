class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = int((str(n)[::-1]))
        d = abs(n-r)
        return d