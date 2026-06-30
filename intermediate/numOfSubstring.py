class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        left = 0
        freq = {'a': 0, 'b': 0, 'c': 0}

        for right in range(len(s)):
            freq[s[right]] += 1

            while all(freq.values()):
                count += len(s) - right
                freq[s[left]] -= 1
                left += 1

        return count