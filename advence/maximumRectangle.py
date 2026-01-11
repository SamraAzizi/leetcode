class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        max_area = 0
        n = len(matrix[0])
        heights = [0] * (n + 1)  # Extra element to handle the stack easily
        
        for row in matrix:
            for j in range(n):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            stack = [-1]
            for i in range(n + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
        
        return max_area