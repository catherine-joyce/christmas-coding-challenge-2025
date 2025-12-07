from solution import Solution


def test_max_3():
    solution = Solution()
    nums = [-2, -1, -1, 1, 2, 3]
    answer = solution.maximumCount(nums)
    assert answer == 3


def test_max_4():
    solution = Solution()
    nums = [5, 20, 66, 1314]
    answer = solution.maximumCount(nums)
    assert answer == 4


def test_max_3_case_2():
    solution = Solution()
    nums = [-3, -2, -1, 0, 0, 1, 2]
    answer = solution.maximumCount(nums)
    assert answer == 3


def test_answer_0():
    solution = Solution()
    nums = [0, 0]
    answer = solution.maximumCount(nums)
    assert answer == 0
