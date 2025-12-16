from day14_solution import Solution


def test_palindrome_121():
    solution = Solution()
    x = 121
    result = solution.isPalindrome(x)
    assert result


def test_palindrome_negative_121():
    solution = Solution()
    x = -121
    result = solution.isPalindrome(x)
    assert not result


def test_palindrome_10():
    solution = Solution()
    x = 10
    result = solution.isPalindrome(x)
    assert not result
