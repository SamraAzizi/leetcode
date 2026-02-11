class Solution(object):
    class SegTree(object):
        def __init__(self, n):
            self.n = n
            size = 4 * n + 5
            self.sum = [0] * size
            self.mn = [0] * size
            self.mx = [0] * size
            self.lazyVal = [0] * size
            self.hasLazy = [False] * size

        def pull(self, v):
            self.sum[v] = self.sum[v << 1] + self.sum[v << 1 | 1]
            self.mn[v] = min(self.mn[v << 1],
                             self.sum[v << 1] + self.mn[v << 1 | 1])
            self.mx[v] = max(self.mx[v << 1],
                             self.sum[v << 1] + self.mx[v << 1 | 1])

        def applySet(self, v, l, r, val):
            length = r - l + 1
            self.sum[v] = val * length
            if val == 0:
                self.mn[v] = 0
                self.mx[v] = 0
            elif val > 0:
                self.mn[v] = val
                self.mx[v] = val * length
            else:
                self.mn[v] = val * length
                self.mx[v] = val
            self.hasLazy[v] = True
            self.lazyVal[v] = val

        def push(self, v, l, r):
            if not self.hasLazy[v] or l == r:
                return
            m = (l + r) >> 1
            self.applySet(v << 1, l, m, self.lazyVal[v])
            self.applySet(v << 1 | 1, m + 1, r, self.lazyVal[v])
            self.hasLazy[v] = False

        def update(self, v, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                self.applySet(v, l, r, val)
                return
            self.push(v, l, r)
            m = (l + r) >> 1
            if ql <= m:
                self.update(v << 1, l, m, ql, qr, val)
            if qr > m:
                self.update(v << 1 | 1, m + 1, r, ql, qr, val)
            self.pull(v)

        def query(self, x):
            if x == 0:
                return -1
            if x < self.mn[1] or x > self.mx[1]:
                return self.n
            pref = [0]
            return self._query(1, 0, self.n - 1, x, pref)

        def _query(self, v, l, r, x, pref):
            if l == r:
                if pref[0] + self.sum[v] == x:
                    return l
                return self.n
            self.push(v, l, r)
            m = (l + r) >> 1
            L = v << 1
            R = v << 1 | 1
            leftMin = pref[0] + self.mn[L]
            leftMax = pref[0] + self.mx[L]
            if x >= leftMin and x <= leftMax:
                return self._query(L, l, m, x, pref)
            else:
                pref[0] += self.sum[L]
                return self._query(R, m + 1, r, x, pref)

    def longestBalanced(self, nums):
        n = len(nums)
        m = max(nums) + 1
        lastPos = [-1] * m
        S = self.SegTree(n)
        total = 0
        ans = 0

        for i in xrange(n):
            if lastPos[nums[i]] != -1:
                S.update(1, 0, n - 1, lastPos[nums[i]], lastPos[nums[i]], 0)
            else:
                if nums[i] % 2:
                    total += 1
                else:
                    total -= 1

            lastPos[nums[i]] = i

            if nums[i] % 2:
                S.update(1, 0, n - 1, i, i, 1)
            else:
                S.update(1, 0, n - 1, i, i, -1)

            p = S.query(total)
            ans = max(ans, i - p)

        return ans