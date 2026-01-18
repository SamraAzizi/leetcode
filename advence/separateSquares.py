

class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        events.sort()

        def union_x_length(intervals):
            intervals.sort()
            total = 0
            cur_start, cur_end = None, None
            for s, e in intervals:
                if cur_start is None:
                    cur_start, cur_end = s, e
                elif s > cur_end:
                    total += cur_end - cur_start
                    cur_start, cur_end = s, e
                else:
                    cur_end = max(cur_end, e)
            if cur_start is not None:
                total += cur_end - cur_start
            return total

        def area_below(h):
            active = []
            prev_y = None
            area = 0.0

            for y, typ, x1, x2 in events:
                if y > h:
                    break

                if prev_y is not None and y > prev_y:
                    area += union_x_length(active) * (y - prev_y)

                if typ == 1:
                    active.append((x1, x2))
                else:
                    active.remove((x1, x2))

                prev_y = y
            if prev_y is not None and prev_y < h:
                area += union_x_length(active) * (h - prev_y)

            return area

        total = area_below(float('inf'))
        target = total / 2

        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        for _ in range(60):
            mid = (low + high) / 2.0
            if area_below(mid) < target:
                low = mid
            else:
                high = mid

        return (low + high) / 2.0