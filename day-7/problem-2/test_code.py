from solution import Solution


def test_all_lowercase():
    solution = Solution()
    s = "LOVELY"
    answer = solution.toLowerCase(s)
    assert answer == "lovely"


def test_hello_world():
    solution = Solution()
    s = "Hello World"
    answer = solution.toLowerCase(s)
    assert answer == "hello world"


def test_no_change():
    solution = Solution()
    s = "hello"
    answer = solution.toLowerCase(s)
    assert answer == "hello"


def test_include_non_alpha_chars():
    solution = Solution()
    s = "al&phaBET"
    answer = solution.toLowerCase(s)
    assert answer == "al&phabet"
