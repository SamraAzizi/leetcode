class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]

        max_area = 0
        for i in range(m):
            sorted_row = sorted(matrix[i], reverse=True)
            for j in range(n):
                max_area = max(max_area, sorted_row[j] * (j + 1))

        return max_area