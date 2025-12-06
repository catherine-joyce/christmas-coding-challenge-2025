class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(nums) + 1):
            result ^= i
        for num in nums:
            result ^= num
        return result
