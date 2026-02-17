class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        if poured == 0:
            return 0.0
        tower = [[0.0] * (i + 1) for i in range(query_row + 1)]
        tower[0][0] = float(poured)
        for r in range(query_row):
            for c in range(r + 1):
                if tower[r][c] > 1.0:
                    excess = tower[r][c] - 1.0
                    tower[r][c] = 1.0
                    tower[r + 1][c] += excess / 2.0
                    tower[r + 1][c + 1] += excess / 2.0
        return min(1.0, tower[query_row][query_glass])