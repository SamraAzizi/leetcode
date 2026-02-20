class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s:
            return ""
        
        # Find all special substrings at the current level
        count = 0
        start = 0
        specials = []
        
        for i, char in enumerate(s):
            count += 1 if char == '1' else -1
            
            # When count becomes 0, we've found a complete special substring
            if count == 0:
                # Recursively process the inner part (without the outer 1 and 0)
                inner = self.makeLargestSpecial(s[start + 1:i])
                # Add back the outer 1 and 0 with the processed inner part
                specials.append('1' + inner + '0')
                start = i + 1
        
        # Sort special substrings in descending order for lexicographically largest result
        specials.sort(reverse=True)
        
        # Combine them
        return ''.join(specials)