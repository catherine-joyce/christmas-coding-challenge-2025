from solution import Solution


def test_123_124():
    solution = Solution()
    assert solution.plusOne([1, 2, 3]) == [1, 2, 4]


def test_9_10():
    solution = Solution()
    assert solution.plusOne([9]) == [1, 0]
