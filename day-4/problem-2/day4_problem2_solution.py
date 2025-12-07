class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def get_number_of_positive_integers(nums):
            low = 0
            high = len(nums) - 1
            num_pos_integers = 0
            found = False
            while low <= high:
                midpoint = (high + low) // 2
                if nums[midpoint] > 0 and nums[midpoint - 1] <= 0 and not found:
                    num_pos_integers = len(nums[midpoint : len(nums)])
                    found = True
                else:
                    if nums[midpoint] <= 0:
                        low = midpoint + 1
                    elif nums[midpoint] > 0:
                        high = midpoint - 1
            return num_pos_integers

        def get_number_of_negative_integers(nums):
            low = 0
            high = len(nums) - 1
            num_neg_integers = 0
            found = False
            while low <= high:
                midpoint = (high + low) // 2
                if nums[midpoint] < 0 and nums[midpoint + 1] >= 0 and not found:
                    num_neg_integers = len(nums[0 : midpoint + 1])
                    found = True
                else:
                    if nums[midpoint] >= 0:
                        high = midpoint - 1
                    elif nums[midpoint] < 0:
                        low = midpoint + 1
            return num_neg_integers

        low = 0
        high = len(nums) - 1
        if (nums[low] > 0 and nums[high] > 0) or (nums[low] < 0 and nums[high] < 0):
            return len(nums)
        else:
            num_positive_integers = get_number_of_positive_integers(nums)
            num_negative_integers = get_number_of_negative_integers(nums)
            return max([num_positive_integers, num_negative_integers])
