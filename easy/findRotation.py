class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        def rotate(matrix):
            # Rotate the matrix 90 degrees clockwise
            return [list(reversed(col)) for col in zip(*matrix)]
        
        for _ in range(4):  # Check all 4 rotations (0, 90, 180, 270 degrees)
            if mat == target:
                return True
            mat = rotate(mat)
        
        return False