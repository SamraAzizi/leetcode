class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # If duplicate found, shrink window from left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add current char to set
            char_set.add(s[right])
            # Update max length
            max_len = max(max_len, right - left + 1)
        
        return max_len
    

solution = Solution()
print(solution.lengthOfLongestSubstring)