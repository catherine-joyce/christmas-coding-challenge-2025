from day15_solution import Solution


def test_abc_true():
    solution = Solution()
    s = "abc"
    t = "ahbgdc"
    result = solution.isSubsequence(s, t)
    assert result


def test_axc_false():
    solution = Solution()
    s = "axc"
    t = "ahbgdc"
    result = solution.isSubsequence(s, t)
    assert not result


def test_s_empty_string():
    solution = Solution()
    s = ""
    t = "ahbgdc"
    result = solution.isSubsequence(s, t)
    assert result
