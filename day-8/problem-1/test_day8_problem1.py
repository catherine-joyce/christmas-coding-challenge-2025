from day8_problem1_solution import Solution

def test_reverse_hello():
    solution = Solution()
    s = ["h","e","l","l","o"]
    assert solution.reverseString(s) == ["o","l","l","e","h"]

def test_reverse_hannah():
    solution = Solution()
    s = ["H","a","n","n","a","h"]
    assert solution.reverseString(s) == ["h","a","n","n","a","H"]