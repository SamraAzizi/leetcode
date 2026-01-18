class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        def max_consecutive(arr):
            arr.sort()
            best = curr = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    curr += 1
                else:
                    curr = 1
                best = max(best, curr)
            return best

        max_h = max_consecutive(hBars) + 1
        max_v = max_consecutive(vBars) + 1

        side = min(max_h, max_v)
        return side * side
