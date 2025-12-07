from day7_problem1_solution import Solution


def test_last_word_5():
    solution = Solution()
    s = "Hello World"
    answer = solution.lengthOfLastWord(s)
    assert answer == 5


def test_last_word_4():
    solution = Solution()
    s = "   fly me   to   the moon  "
    answer = solution.lengthOfLastWord(s)
    assert answer == 4
