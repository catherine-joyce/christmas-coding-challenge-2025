from day5_solution import Solution


def test_reverse_letters():
    solution = Solution()
    s = "ab-cd"
    answer = solution.reverseOnlyLetters(s)
    assert answer == "dc-ba"


def test_reverse_letters_case_2():
    solution = Solution()
    s = "Test1ng-Leet=code-Q!"
    answer = solution.reverseOnlyLetters(s)
    assert answer == "Qedo1ct-eeLg=ntse-T!"


def test_reverse_letters_case_3():
    solution = Solution()
    s = "7_28]"
    answer = solution.reverseOnlyLetters(s)
    assert answer == "7_28]"
