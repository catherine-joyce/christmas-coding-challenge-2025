from day16_solution import Solution


def test_lowest_common_number_2():
    solution = Solution()
    nums1 = [1, 2, 3]
    nums2 = [2, 4]
    result = solution.getCommon(nums1, nums2)
    assert result == 2


def test_lowest_common_number_2_case_2():
    solution = Solution()
    nums1 = [1, 2, 3, 6]
    nums2 = [2, 3, 4, 5]
    result = solution.getCommon(nums1, nums2)
    assert result == 2
