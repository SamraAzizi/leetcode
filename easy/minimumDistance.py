class Solution(object):
    def minimumDistance(self, nums):
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        m = float('inf')

        for num in d:
            if d[num] >= 3:
                idx = []

                for i, v in enumerate(nums):
                    if v == num:
                        idx.append(i)
                for i in range(len(idx) - 2):
                    i1, i2, i3 = idx[i], idx[i+1], idx[i+2]
                    m = min(m, abs(i1-i2) + abs(i2-i3) + abs(i1-i3))

        return m if m != float('inf') else -1