from day13_solution import Solution


def test_reverse_bits():
    n = 43261596
    solution = Solution()
    result = solution.reverseBits(n)
    assert result == 964176192
