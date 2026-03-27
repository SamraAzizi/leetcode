class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] != k:
                    return False
        
        return True