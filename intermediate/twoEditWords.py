class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        def isTwoEditDistance(s1, s2):
            diffCount = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diffCount += 1
                    if diffCount > 2:
                        return False
            return diffCount <= 2

        result = []
        for query in queries:
            for word in dictionary:
                if isTwoEditDistance(query, word):
                    result.append(query)
                    break

        return result