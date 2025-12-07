class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)):
            num = nums[i]
            if i == (len(nums) - 1):
                if nums[i] == nums[i-1]:
                    result ^= num ^ num
                else:
                    result ^= num
            elif nums[i] == nums[i-1] or nums[i] == nums[i+1]:
                result ^= num ^ num
            else:
                result ^= num
        return result