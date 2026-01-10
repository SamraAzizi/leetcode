class Solution(object):
    def repeatedNTimes(self, A):
        seen = set()
        for num in A:
            if num in seen:
                return num
            seen.add(num)