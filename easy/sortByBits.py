class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Sort the array based on the number of 1's in the binary representation
        # If two numbers have the same number of 1's, sort them by their value
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))