from solution import Solution


def test_friends_134_outputs_314():
    solution = Solution()
    order = [3, 1, 2, 5, 4]
    friends = [1, 3, 4]
    assert solution.recoverOrder(order, friends) == [3, 1, 4]


def test_friends_25_outputs_52():
    solution = Solution()
    order = [1, 4, 5, 3, 2]
    friends = [2, 5]
    assert solution.recoverOrder(order, friends) == [5, 2]


def test_friends_12_outputs_12():
    solution = Solution()
    order = [1, 2, 3]
    friends = [1, 2]
    assert solution.recoverOrder(order, friends) == [1, 2]
