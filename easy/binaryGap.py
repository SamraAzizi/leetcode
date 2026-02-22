class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Convert the number to binary and find the positions of '1's
        binary_representation = bin(n)[2:]  # Get binary representation as a string
        positions = [i for i, bit in enumerate(binary_representation) if bit == '1']
        
        # Calculate the maximum distance between consecutive '1's
        max_distance = 0
        for i in range(1, len(positions)):
            distance = positions[i] - positions[i - 1]
            max_distance = max(max_distance, distance)
        
        return max_distance