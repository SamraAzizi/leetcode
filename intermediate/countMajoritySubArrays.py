class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        n = len(nums)

        for i in range(n):
            majority_count = 0
            for j in range(i, n):
                if nums[j] == target:
                    majority_count += 1
                if majority_count > (j - i + 1) // 2:
                    count += 1

        return count