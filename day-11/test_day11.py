from day11_solution import Solution

def test_n_3():
    solution = Solution()
    n = 3
    result = solution.fizzBuzz(n)
    assert result == ["1","2","Fizz"]

def test_n_5():
    solution = Solution()
    n = 5
    result = solution.fizzBuzz(n)
    assert result == ["1","2","Fizz","4","Buzz"] 

def test_n_15():
    solution = Solution()
    n = 15
    result = solution.fizzBuzz(n)
    assert result == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]