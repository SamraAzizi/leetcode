class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])

        # Build prefix sum matrix
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = (
                    mat[i - 1][j - 1]
                    + prefix_sum[i - 1][j]
                    + prefix_sum[i][j - 1]
                    - prefix_sum[i - 1][j - 1]
                )

        # Check if a square of given size exists with sum <= threshold
        def can_find_square_of_size(size):
            for i in range(size, m + 1):
                for j in range(size, n + 1):
                    total = (
                        prefix_sum[i][j]
                        - prefix_sum[i - size][j]
                        - prefix_sum[i][j - size]
                        + prefix_sum[i - size][j - size]
                    )
                    if total <= threshold:
                        return True
            return False

        left, right = 0, min(m, n)
        result = 0

        # Binary search on side length
        while left <= right:
            mid = (left + right) // 2
            if can_find_square_of_size(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result