class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        count = {}
        sumIndices = {}

        for i, num in enumerate(nums):
            if num in count:
                result[i] += count[num] * i - sumIndices[num]
            count[num] = count.get(num, 0) + 1
            sumIndices[num] = sumIndices.get(num, 0) + i

        count.clear()
        sumIndices.clear()

        for i in range(n - 1, -1, -1):
            num = nums[i]
            if num in count:
                result[i] += sumIndices[num] - count[num] * i
            count[num] = count.get(num, 0) + 1
            sumIndices[num] = sumIndices.get(num, 0) + i

        return result