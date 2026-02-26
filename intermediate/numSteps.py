class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        num = 0
        for i in range(len(s)):
            num = num * 2 + int(s[i])
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            steps += 1
        return steps