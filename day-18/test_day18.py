from day18_solution import Solution


def test_abc():
    solution = Solution()
    words = ["a", "b", "c", "ab", "bc", "abc"]
    s = "abc"
    result = solution.countPrefixes(words, s)
    assert result == 3


def test_aa():
    solution = Solution()
    words = ["a", "a"]
    s = "aa"
    result = solution.countPrefixes(words, s)
    assert result == 2


def test_w():
    solution = Solution()
    words = [
        "feh",
        "w",
        "w",
        "lwd",
        "c",
        "s",
        "vk",
        "zwlv",
        "n",
        "w",
        "sw",
        "qrd",
        "w",
        "w",
        "mqe",
        "w",
        "w",
        "w",
        "gb",
        "w",
        "qy",
        "xs",
        "br",
        "w",
        "rypg",
        "wh",
        "g",
        "w",
        "w",
        "fh",
        "w",
        "w",
        "sccy",
    ]
    s = "w"
    result = solution.countPrefixes(words, s)
    assert result == 14
