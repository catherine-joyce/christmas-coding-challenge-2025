from day17_solution import Solution


def test_iloveleetcode_true():
    solution = Solution()
    s = "iloveleetcode"
    words = ["i", "love", "leetcode", "apples"]
    result = solution.isPrefixString(s, words)
    assert result


def test_iloveleetcode_false():
    solution = Solution()
    s = "iloveleetcode"
    words = ["apples", "i", "love", "leetcode"]
    result = solution.isPrefixString(s, words)
    assert not result
