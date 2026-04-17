class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        min_distance = float('inf')

        for i in range(n):
            if words[i] == target:
                distance = min(abs(i - startIndex), n - abs(i - startIndex))
                min_distance = min(min_distance, distance)

        return min_distance if min_distance != float('inf') else -1