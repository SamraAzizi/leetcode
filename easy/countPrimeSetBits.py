class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # List of prime numbers up to 20 (since the maximum number of set bits in a 32-bit integer is 32)
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19}
        
        count = 0
        
        for num in range(left, right + 1):
            # Count the number of set bits in num
            set_bits = bin(num).count('1')
            # Check if the count of set bits is prime
            if set_bits in prime_set:
                count += 1
        
        return count