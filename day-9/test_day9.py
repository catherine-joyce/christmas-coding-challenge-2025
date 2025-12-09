from day9_solution import Solution


def test_reverse_sentence():
    solution = Solution()
    s = "Let's take LeetCode contest"
    result = solution.reverseWords(s)
    assert result == "s'teL ekat edoCteeL tsetnoc"


def test_reverse_sentence_case_2():
    solution = Solution()
    s = "Mr Ding"
    result = solution.reverseWords(s)
    assert result == "rM gniD"
