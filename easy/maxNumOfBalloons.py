class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        balloon_count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for char in text:
            if char in balloon_count:
                balloon_count[char] += 1

        balloon_count['l'] //= 2
        balloon_count['o'] //= 2

        return min(balloon_count.values())