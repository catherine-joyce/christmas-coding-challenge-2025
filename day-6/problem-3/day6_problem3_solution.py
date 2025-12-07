class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        string_list = []
        i = 0
        for j in range(len(nums)):
            if (j == len(nums) - 1) or (nums[j] + 1 != nums[j + 1]):
                if i == j:
                    string_list.append(str(nums[i]))
                else:
                    string_list.append(str(nums[i]) + "->" + str(nums[j]))
                i = j + 1
        return string_list
