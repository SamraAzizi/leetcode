class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums)
        # Create a set of existing binary strings for O(1) lookups
        existing = set(nums)

        # Generate all possible binary strings of length n
        for i in range(1 << n):  # 2^n possible combinations
            candidate = format(i, '0' + str(n) + 'b')  # Convert to binary string with leading zeros
            if candidate not in existing:
                return candidate

        return ""  # This line should never be reached since there are 2^n possible strings and only n are given