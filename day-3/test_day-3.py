from day3_solution import Solution


def test_remove_duplicates():
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    answer = solution.removeDuplicates(nums)
    assert answer == 5
    assert nums[0:answer] == [0, 1, 2, 3, 4]


def test_remove_duplicates_case_2():
    solution = Solution()
    nums = [1, 1, 2]
    answer = solution.removeDuplicates(nums)
    assert answer == 2
    assert nums[0:answer] == [1, 2]


def test_remove_duplicates_case_3():
    solution = Solution()
    nums = [0, 0, 0, 3]
    answer = solution.removeDuplicates(nums)
    assert answer == 2
    assert nums[0:answer] == [0, 3]


def test_remove_duplicates_case_4():
    solution = Solution()
    nums = [0, 0, 0, 1, 1, 1, 99]
    answer = solution.removeDuplicates(nums)
    assert answer == 3
    assert nums[0:answer] == [0, 1, 99]
