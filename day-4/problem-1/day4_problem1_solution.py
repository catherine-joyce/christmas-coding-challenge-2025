class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        found = False
        index = -1

        while low <= high and not found:
            midpoint = (high + low) // 2
            if nums[midpoint] == target:
                found = True
                index = midpoint
            else:
                if target < nums[midpoint]:
                    high = midpoint - 1
                else:
                    low = midpoint + 1
        return index
