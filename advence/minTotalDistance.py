class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        nums = []
        for pos, cap in factory:
            nums.extend([pos] * cap)

        n, m = len(robot), len(nums)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        def solve(i, j):
            if i >= n:
                return 0
            if j >= m:
                return float('inf')

            if dp[i][j] != -1:
                return dp[i][j]

            take = abs(robot[i] - nums[j]) + solve(i + 1, j + 1)
            notake = solve(i, j + 1)

            dp[i][j] = min(take, notake)
            return dp[i][j]

        return solve(0, 0)