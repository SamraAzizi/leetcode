class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def get_f(s):
            parity = [collections.Counter(), collections.Counter()]
            for i in range(len(s)):
                parity[i % 2][s[i]]+=1
            return parity
        
        return get_f(s1) == get_f(s2)