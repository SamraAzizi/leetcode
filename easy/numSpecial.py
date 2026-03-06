class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if sum(mat[i]) == 1 and sum(mat[k][j] for k in range(len(mat))) == 1:
                        count += 1
        return count