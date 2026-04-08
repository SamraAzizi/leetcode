class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        for l, r, k, v in queries:
            i = l
            while i <= r:
                nums[i] = (nums[i] * v) % MOD
                i += k

        ans = 0
        for num in nums:
            ans ^= num

        return ans