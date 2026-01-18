class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):

        MOD = 10**9 + 7

        h = [1] + sorted(hFences) + [m]
        v = [1] + sorted(vFences) + [n]

        h_dist = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_dist.add(h[j] - h[i])

        ans = 0
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                d = v[j] - v[i]
                if d in h_dist:
                    ans = max(ans, d)

        if ans == 0:
            return -1
        return (ans * ans) % MOD
    