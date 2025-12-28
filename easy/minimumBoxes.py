class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        boxes_needed = 0
        current_capacity = 0
        for c in capacity:
            if current_capacity >= total_apples:
                break
            current_capacity += c
            boxes_needed += 1
        return boxes_needed