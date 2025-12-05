from solution import Solution

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
