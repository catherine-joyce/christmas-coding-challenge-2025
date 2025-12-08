from day8_problem2_solution import Solution

def test_reverse_abcdefg():
    solution = Solution()
    s = "abcdefg"
    k = 2 
    assert solution.reverseStr(s, k) ==  "bacdfeg"


def test_reverse_abcd():
    solution = Solution()
    s = "abcd"
    k = 2 
    assert solution.reverseStr(s, k) ==  "bacd"

def test_reverse_k_equals_3():
    solution = Solution()
    s = "abcdef"
    k = 3
    assert solution.reverseStr(s, k) ==  "cbadef"

def test_reverse_k_equals_1():
    solution = Solution()
    s = "abcdefg"
    k = 1
    assert solution.reverseStr(s, k) ==  "abcdefg"

def test_reverse_k_equals_4():
    solution = Solution()
    s = "abcd"
    k = 4
    assert solution.reverseStr(s, k) ==  "dcba"

def test_reverse_k_equals_4():
    solution = Solution()
    s = "abcdefg"
    k = 8
    assert solution.reverseStr(s, k) ==  "gfedcba"

def test_reverse_k_equals_39():
    solution = Solution()
    s = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
    k = 39
    assert solution.reverseStr(s, k) == "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi"