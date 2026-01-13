class Solution(object):
    def separateSquares(self, squares):
        def balance(h):
            below = 0.0
            above = 0.0

            for _, y, l in squares:
                top = y + l
                area = l * l

                if h <= y:
                    above += area
                elif h >= top:
                    below += area
                else:
                    cut = l * (h - y)
                    below += cut
                    above += area - cut

            return below - above

        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        for _ in range(60):
            mid = (low + high) / 2.0
            if balance(mid) < 0:
                low = mid
            else:
                high = mid

        return (low + high) / 2.0
