from solution import Solution


def test_add_binary_100():
    solution = Solution()
    a = "11"
    b = "1"
    answer = solution.addBinary(a, b)
    assert answer == "100"


def test_add_binary_10101():
    solution = Solution()
    a = "1010"
    b = "1011"
    answer = solution.addBinary(a, b)
    assert answer == "10101"
