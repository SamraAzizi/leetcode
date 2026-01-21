class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def ctz(v):
            # count trailing zeros
            return (v & -v).bit_length() - 1
        
        ans = []
        for n in nums:
            if n % 2 == 0:
                ans.append(-1)
                continue
            k = ctz(n + 1)  # number of trailing 1s in n
            mask = 1 << (k - 1)
            x = n & (~mask)
            ans.append(x)
        return ans
        