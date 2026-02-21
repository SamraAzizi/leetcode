class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        prev_run_length = 0
        current_run_length = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_run_length += 1
            else:
                count += min(prev_run_length, current_run_length)
                prev_run_length = current_run_length
                current_run_length = 1
        
        count += min(prev_run_length, current_run_length)
        
        return count