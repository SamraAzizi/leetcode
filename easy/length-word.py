class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()  # Remove leading and trailing spaces
        word = s.rfind(' ')  # Find the index of the last space
        if word == -1:
            return len(s)  # If no space is found, the entire string is the last word
        return len(s) - word - 1  # Calculate the length of the last word
    
solution = Solution()
print(solution.lengthOfLastWord("Hello World"))  # Output: 5