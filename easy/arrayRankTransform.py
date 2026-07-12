class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]



        """
        s = list(set(arr))
        s.sort()
        rank = {}
        for index, value in enumerate(s):
            rank[value] = index + 1 
        
        return [rank[x] for x in arr]
