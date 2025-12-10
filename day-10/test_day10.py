from day10_solution import Solution


def test_3():
    s = "III"
    solution = Solution()
    result = solution.romanToInt(s)
    assert result == 3


def test_58():
    s = "LVIII"
    solution = Solution()
    result = solution.romanToInt(s)
    assert result == 58


def test_1994():
    s = "MCMXCIV"
    solution = Solution()
    result = solution.romanToInt(s)
    assert result == 1994
