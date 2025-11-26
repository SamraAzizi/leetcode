class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Compare with each subsequent string
        for i in range(1, len(strs)):
            current_string = strs[i]
            
            # Reduce the prefix until it matches the beginning of current string
            while current_string.find(prefix) != 0:
                prefix = prefix[:-1]  # Remove last character
                if not prefix:  # If prefix becomes empty
                    return ""
        
        return prefix

# Test cases
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"