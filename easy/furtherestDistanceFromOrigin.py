class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        L = 0
        R = 0
        B = 0

        for c in moves:
            if c == 'L':
                L += 1
            elif c == 'R':
                R += 1
            else:
                B += 1

        return abs(L - R) + B