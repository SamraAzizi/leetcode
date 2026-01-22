class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            found = -1
            # Try all possible x from 0 up to num (since x OR (x+1) can't exceed num in some constraints)
            # Actually x can be up to num, but we need to find minimal x
            for x in range(num):
                if (x | (x + 1)) == num:
                    found = x
                    break
            ans.append(found)
        return ans