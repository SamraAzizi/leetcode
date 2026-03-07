class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)

        # mz = mismatches if index should contain '0'
        # mo = mismatches if index should contain '1'
        missed_zeroes = [0, 0]
        missed_ones = [0, 0]

        # Count mismatches in the base string
        for i in range(n):
            # Use the parity (i % 2) to mark even/odd mismatch
            if s[i] != "0":
                missed_zeroes[i % 2] += 1
            if s[i] != "1":
                missed_ones[i % 2] += 1

        # Initial minimum move 2 cost to fix 
        res = min(missed_zeroes[0] + missed_ones[1], missed_zeroes[1] + missed_ones[0])

        # Simulate rotations
        for i in range(n):

            # Remove mismatch contribution of the character leaving the front
            if s[i] == "0":
                missed_ones[0] -= 1
            else:
                missed_zeroes[0] -= 1

            # Parity of indices flips after rotation
            missed_zeroes[0], missed_zeroes[1] = missed_zeroes[1], missed_zeroes[0]
            missed_ones[0], missed_ones[1] = missed_ones[1], missed_ones[0]

            # Add the character back at the end
            if s[i] == "0":
                missed_ones[(n - 1) % 2] += 1
            else:
                missed_zeroes[(n - 1) % 2] += 1

            # Update minimum flips
            res = min(res, missed_zeroes[0] + missed_ones[1], missed_zeroes[1] + missed_ones[0])

        return res