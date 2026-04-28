#translated using AI
class Solution:
    def minOperations(self, grid, x):
        arr = []

        for row in grid:
            for val in row:
                arr.append(val)

        arr.sort()
        median = arr[len(arr) // 2]

        operations = 0
        for num in arr:
            diff = abs(num - median)
            if diff % x != 0:
                return -1
            operations += diff // x

        return operations