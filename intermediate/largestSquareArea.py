class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        n = len(bottomLeft)
        max_area = 0

        for i in range(n):
            for j in range(i + 1, n):
                left   = max(bottomLeft[i][0], bottomLeft[j][0])
                right  = min(topRight[i][0], topRight[j][0])
                bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                top    = min(topRight[i][1], topRight[j][1])

                if left < right and bottom < top:
                    side = min(right - left, top - bottom)
                    max_area = max(max_area, side * side)

        return max_area