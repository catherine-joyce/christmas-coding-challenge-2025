from solution import Solution

def test_find_9():
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    answer = solution.search(nums, target)
    assert answer == 4

def test_target_not_in_list():
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 2
    answer = solution.search(nums, target)
    assert answer == -1
