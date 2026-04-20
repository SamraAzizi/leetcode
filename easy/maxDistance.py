#translated using AI
class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        maxDist = 0

        # Compare with first house
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                maxDist = i
                break

        # Compare with last house
        for i in range(n):
            if colors[i] != colors[n - 1]:
                maxDist = max(maxDist, n - 1 - i)
                break

        return maxDist