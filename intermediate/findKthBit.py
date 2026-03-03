class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s="0"
        for i in range(n):
            invert="".join("1" if b == "0" else "0" for b in s)
            reverse = invert[::-1]
            s= s+ "1"+ reverse
        return s[k-1]


        