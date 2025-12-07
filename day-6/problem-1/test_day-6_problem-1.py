from day6_problem1_solution import Solution


def test_first_index():
    solution = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    answer = solution.strStr(haystack, needle)
    assert answer == 0


def test_first_index_case_2():
    solution = Solution()
    haystack = "leetcode"
    needle = "leeto"
    answer = solution.strStr(haystack, needle)
    assert answer == -1


def test_first_index_case_3():
    solution = Solution()
    haystack = "mississippi"
    needle = "issip"
    answer = solution.strStr(haystack, needle)
    assert answer == 4


def test_first_index_case_4():
    solution = Solution()
    haystack = "a"
    needle = "a"
    answer = solution.strStr(haystack, needle)
    assert answer == 0
