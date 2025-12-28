class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        n = len(customers)
        max_score = 0
        best_hour = 0
        current_score = 0

        for i in range(n):
            if customers[i] == 'Y':
                current_score += 1
            else:
                current_score -= 1

            if current_score > max_score:
                max_score = current_score
                best_hour = i + 1

        return best_hour