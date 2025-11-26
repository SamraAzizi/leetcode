class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {
            "{": "}",
            "[": "]",
            "(": "}"
        }

        stack = []  # Initialize an empty stack to keep track of opening brackets
        for char in s:
            if char in bracket_map:
                stack.append(char)
            elif char in bracket_map.values():
                if not stack or bracket_map[stack[-1]] != char:
                    return False
                stack.pop()
        return len(stack) == 0
    
solution = Solution()
print(solution.isValid(""))