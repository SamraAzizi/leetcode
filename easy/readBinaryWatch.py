class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []
        
        # Try all possible hours (0-11)
        for hour in range(12):
            # Try all possible minutes (0-59)
            for minute in range(60):
                # Count bits set to 1 in hour and minute
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    # Format with Python 2.7 compatible syntax
                    result.append("{}:{:02d}".format(hour, minute))
        
        return result