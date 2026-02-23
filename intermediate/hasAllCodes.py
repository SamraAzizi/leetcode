class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # Create a set to store unique binary codes of length k
        seen = set()
        
        # Iterate through the string and extract all substrings of length k
        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            seen.add(substring)
        
        # The total number of possible binary codes of length k is 2^k
        total_codes = 2 ** k
        
        # Check if we have seen all possible codes
        return len(seen) == total_codes