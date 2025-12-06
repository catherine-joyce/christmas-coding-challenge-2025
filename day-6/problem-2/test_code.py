from solution import Solution


def test_missing_number_1():
    solution = Solution()
    nums = [3, 0, 1]
    answer = solution.missingNumber(nums)
    assert answer == 2


def test_missing_number_2():
    solution = Solution()
    nums = [0, 1]
    answer = solution.missingNumber(nums)
    assert answer == 2


def test_missing_number_3():
    solution = Solution()
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    answer = solution.missingNumber(nums)
    assert answer == 8
