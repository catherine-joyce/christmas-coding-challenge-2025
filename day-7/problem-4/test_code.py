from solution import Solution


def test_get_single_number_99():
    solution = Solution()
    nums = [0,1,0,1,0,1,99]
    answer = solution.singleNumber(nums)
    assert answer == 99
