class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        
        total_happiness = 0
        
        # Pick k children
        for i in range(k):
            # Happiness value after i turns of decreasing
            # Each child's happiness decreases by i when selected at turn i
            current_happiness = max(0, happiness[i] - i)
            total_happiness += current_happiness
        
        return total_happiness