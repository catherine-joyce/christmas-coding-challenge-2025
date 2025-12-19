from day19_solution import Solution


def test_USA():
    solution = Solution()
    word = "USA"
    result = solution.detectCapitalUse(word)
    assert result


def test_flag():
    solution = Solution()
    word = "FlaG"
    result = solution.detectCapitalUse(word)
    assert not result
