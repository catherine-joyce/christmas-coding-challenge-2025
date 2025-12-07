from day6_problem3_solution import Solution


def test_generate_ranges():
    solution = Solution()
    nums = [0, 1, 2, 4, 5, 7]
    answer = solution.summaryRanges(nums)
    assert answer == ["0->2", "4->5", "7"]


def test_generate_ranges_2():
    solution = Solution()
    nums = [0, 2, 3, 4, 6, 8, 9]
    answer = solution.summaryRanges(nums)
    assert answer == ["0", "2->4", "6", "8->9"]
